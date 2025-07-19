import React, { useEffect } from 'react';
import { useSystemStore } from '../../store/systemStore';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export const SuperAdminDashboard: React.FC = () => {
  const { 
    dashboardStats, 
    systemStatus, 
    fetchDashboardStats, 
    startSystem, 
    stopSystem, 
    isLoading, 
    error 
  } = useSystemStore();

  useEffect(() => {
    fetchDashboardStats();
  }, [fetchDashboardStats]);

  const handleSystemControl = async (action: 'start' | 'stop') => {
    try {
      if (action === 'start') {
        await startSystem();
      } else {
        await stopSystem();
      }
      // Refresh dashboard stats after system control
      await fetchDashboardStats();
    } catch (error) {
      console.error('System control failed:', error);
    }
  };

  const formatUptime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${minutes}m`;
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Super Admin Dashboard</h1>
        <p className="text-gray-600">System overview and master controls</p>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
          <p className="text-sm">{error}</p>
        </div>
      )}

      {/* System Status and Control */}
      <Card>
        <CardHeader>
          <CardTitle>Face Recognition System Control</CardTitle>
          <CardDescription>
            Monitor and control the core face recognition system
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-between">
            <div className="space-y-2">
              <div className="flex items-center space-x-3">
                <div 
                  className={`h-3 w-3 rounded-full ${
                    systemStatus?.is_running ? 'bg-green-500' : 'bg-red-500'
                  }`}
                />
                <span className="font-medium">
                  Status: {systemStatus?.is_running ? 'Running' : 'Stopped'}
                </span>
              </div>
              {systemStatus?.is_running && systemStatus.uptime > 0 && (
                <p className="text-sm text-gray-600">
                  Uptime: {formatUptime(systemStatus.uptime)}
                </p>
              )}
            </div>
            <div className="space-x-2">
              <Button
                onClick={() => handleSystemControl('start')}
                disabled={isLoading || systemStatus?.is_running}
                loading={isLoading}
                variant="default"
              >
                Start System
              </Button>
              <Button
                onClick={() => handleSystemControl('stop')}
                disabled={isLoading || !systemStatus?.is_running}
                loading={isLoading}
                variant="destructive"
              >
                Stop System
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* System Metrics */}
      {dashboardStats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Total Employees</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-primary-600">
                {dashboardStats.totalEmployees}
              </div>
              <p className="text-sm text-gray-600 mt-1">Registered in system</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Present Today</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-green-600">
                {dashboardStats.presentEmployees}
              </div>
              <p className="text-sm text-gray-600 mt-1">Currently present</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Active Cameras</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-blue-600">
                {dashboardStats.activeCameras}/{dashboardStats.totalCameras}
              </div>
              <p className="text-sm text-gray-600 mt-1">Online cameras</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Today's Detections</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-purple-600">
                {dashboardStats.todayAttendance}
              </div>
              <p className="text-sm text-gray-600 mt-1">Face recognitions</p>
            </CardContent>
          </Card>
        </div>
      )}

      {/* System Information */}
      {systemStatus && (
        <Card>
          <CardHeader>
            <CardTitle>System Information</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="text-sm font-medium text-gray-700">Cameras Active</label>
                <p className="text-lg font-semibold">{systemStatus.cam_count}</p>
              </div>
              <div>
                <label className="text-sm font-medium text-gray-700">Faces Detected</label>
                <p className="text-lg font-semibold">{systemStatus.faces_detected}</p>
              </div>
              <div>
                <label className="text-sm font-medium text-gray-700">Attendance Count</label>
                <p className="text-lg font-semibold">{systemStatus.attendance_count}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Quick Actions */}
      <Card>
        <CardHeader>
          <CardTitle>Quick Actions</CardTitle>
          <CardDescription>
            Frequently used administrative tasks
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <Button variant="outline" className="h-20 flex-col">
              <span className="text-lg mb-1">👥</span>
              <span>Manage Users</span>
            </Button>
            <Button variant="outline" className="h-20 flex-col">
              <span className="text-lg mb-1">📹</span>
              <span>Camera Settings</span>
            </Button>
            <Button variant="outline" className="h-20 flex-col">
              <span className="text-lg mb-1">📊</span>
              <span>View Logs</span>
            </Button>
            <Button variant="outline" className="h-20 flex-col">
              <span className="text-lg mb-1">⚙️</span>
              <span>System Config</span>
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};