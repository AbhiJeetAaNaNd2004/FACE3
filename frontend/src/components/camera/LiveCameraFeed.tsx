import React, { useRef, useEffect, useState } from 'react';
import { Camera } from '../../types';
import { useWebSocket } from '../../hooks/useWebSocket';

interface LiveCameraFeedProps {
  camera: Camera;
  className?: string;
  onError?: (error: string) => void;
  showControls?: boolean;
}

export const LiveCameraFeed: React.FC<LiveCameraFeedProps> = ({
  camera,
  className = '',
  onError,
  showControls = true
}) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [detections, setDetections] = useState<any[]>([]);

  // WebSocket connection for real-time updates
  const { isConnected } = useWebSocket({
    url: `ws://localhost:8000/ws/camera/${camera.id}`,
    onMessage: (message) => {
      if (message.type === 'detection') {
        setDetections(message.data.detections || []);
        drawDetections(message.data.detections || []);
      } else if (message.type === 'frame') {
        updateVideoFrame(message.data.frame);
      }
    },
    onError: (error) => {
      console.error('Camera WebSocket error:', error);
      setError('Failed to connect to camera stream');
    }
  });

  const updateVideoFrame = (frameData: string) => {
    if (videoRef.current) {
      // Convert base64 frame to blob and create object URL
      const binary = atob(frameData);
      const bytes = new Uint8Array(binary.length);
      for (let i = 0; i < binary.length; i++) {
        bytes[i] = binary.charCodeAt(i);
      }
      const blob = new Blob([bytes], { type: 'image/jpeg' });
      const url = URL.createObjectURL(blob);
      
      // Create image element and draw to canvas
      const img = new Image();
      img.onload = () => {
        if (canvasRef.current) {
          const canvas = canvasRef.current;
          const ctx = canvas.getContext('2d');
          if (ctx) {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);
          }
        }
        URL.revokeObjectURL(url);
      };
      img.src = url;
    }
  };

  const drawDetections = (detections: any[]) => {
    if (!canvasRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Clear previous detections
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw detection boxes
    detections.forEach(detection => {
      const { bbox, confidence, class_name, employee_id, employee_name } = detection;
      
      if (bbox && bbox.length === 4) {
        const [x, y, width, height] = bbox;
        
        // Draw bounding box
        ctx.strokeStyle = employee_id ? '#10B981' : '#EF4444'; // Green for recognized, red for unknown
        ctx.lineWidth = 2;
        ctx.strokeRect(x, y, width, height);
        
        // Draw label background
        const label = employee_name || `Unknown (${(confidence * 100).toFixed(1)}%)`;
        const labelHeight = 20;
        
        ctx.fillStyle = employee_id ? '#10B981' : '#EF4444';
        ctx.fillRect(x, y - labelHeight, ctx.measureText(label).width + 10, labelHeight);
        
        // Draw label text
        ctx.fillStyle = '#FFFFFF';
        ctx.font = '12px Arial';
        ctx.fillText(label, x + 5, y - 5);
      }
    });
  };

  const startStream = async () => {
    try {
      setError(null);
      
      if (camera.stream_url) {
        // For RTSP or HTTP streams
        if (videoRef.current) {
          videoRef.current.src = camera.stream_url;
          await videoRef.current.play();
          setIsPlaying(true);
        }
      } else {
        // For webcam access
        const stream = await navigator.mediaDevices.getUserMedia({ 
          video: { 
            width: { ideal: 1280 },
            height: { ideal: 720 }
          } 
        });
        
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
          await videoRef.current.play();
          setIsPlaying(true);
        }
      }
    } catch (err) {
      const errorMessage = 'Failed to start camera stream';
      setError(errorMessage);
      onError?.(errorMessage);
      console.error('Camera stream error:', err);
    }
  };

  const stopStream = () => {
    if (videoRef.current) {
      if (videoRef.current.srcObject) {
        const stream = videoRef.current.srcObject as MediaStream;
        stream.getTracks().forEach(track => track.stop());
        videoRef.current.srcObject = null;
      } else {
        videoRef.current.src = '';
      }
      setIsPlaying(false);
    }
  };

  const toggleStream = () => {
    if (isPlaying) {
      stopStream();
    } else {
      startStream();
    }
  };

  useEffect(() => {
    return () => {
      stopStream();
    };
  }, []);

  return (
    <div className={`relative bg-black rounded-lg overflow-hidden ${className}`}>
      {/* Video Element (hidden, used for stream source) */}
      <video
        ref={videoRef}
        className="hidden"
        muted
        playsInline
        onError={() => setError('Video stream error')}
      />
      
      {/* Canvas for displaying frames and detections */}
      <canvas
        ref={canvasRef}
        className="w-full h-full object-contain"
        style={{ maxHeight: '400px' }}
      />
      
      {/* Overlay Information */}
      <div className="absolute top-2 left-2">
        <div className="bg-black bg-opacity-75 text-white px-2 py-1 rounded text-xs">
          {camera.name}
        </div>
        {isConnected && (
          <div className="bg-green-600 bg-opacity-75 text-white px-2 py-1 rounded text-xs mt-1">
            Live
          </div>
        )}
      </div>

      {/* Detection Count */}
      {detections.length > 0 && (
        <div className="absolute top-2 right-2">
          <div className="bg-blue-600 bg-opacity-75 text-white px-2 py-1 rounded text-xs">
            {detections.length} Detection{detections.length !== 1 ? 's' : ''}
          </div>
        </div>
      )}

      {/* Error Display */}
      {error && (
        <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-75">
          <div className="text-red-400 text-center">
            <div className="text-4xl mb-2">⚠️</div>
            <div>{error}</div>
          </div>
        </div>
      )}

      {/* No Stream Placeholder */}
      {!isPlaying && !error && (
        <div className="absolute inset-0 flex items-center justify-center bg-gray-800">
          <div className="text-gray-400 text-center">
            <div className="text-4xl mb-2">📹</div>
            <div>Camera stream not active</div>
          </div>
        </div>
      )}

      {/* Controls */}
      {showControls && (
        <div className="absolute bottom-2 left-2 right-2 flex justify-between items-center">
          <button
            onClick={toggleStream}
            className={`px-3 py-1 rounded text-xs font-medium ${
              isPlaying
                ? 'bg-red-600 hover:bg-red-700 text-white'
                : 'bg-green-600 hover:bg-green-700 text-white'
            }`}
          >
            {isPlaying ? 'Stop' : 'Start'}
          </button>
          
          <div className="text-white text-xs bg-black bg-opacity-50 px-2 py-1 rounded">
            {camera.location}
          </div>
        </div>
      )}
    </div>
  );
};