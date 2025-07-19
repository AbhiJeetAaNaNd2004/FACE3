import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import { UserRole } from './types';
import { LoginPage } from './pages/login/LoginPage';
import { DashboardLayout } from './components/layout/DashboardLayout';
import { SuperAdminDashboard } from './pages/super-admin/SuperAdminDashboard';

// Protected Route Component
interface ProtectedRouteProps {
  children: React.ReactNode;
  requiredRole?: UserRole;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children, requiredRole }) => {
  const { isAuthenticated, user, isLoading } = useAuthStore();

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (!isAuthenticated || !user) {
    return <Navigate to="/login" replace />;
  }

  if (requiredRole) {
    const roleHierarchy = {
      [UserRole.EMPLOYEE]: 1,
      [UserRole.ADMIN]: 2,
      [UserRole.SUPER_ADMIN]: 3,
    };

    if (roleHierarchy[user.role] < roleHierarchy[requiredRole]) {
      return <Navigate to="/unauthorized" replace />;
    }
  }

  return <>{children}</>;
};

// Placeholder components for other dashboards
const AdminDashboard: React.FC = () => (
  <div className="space-y-6">
    <div>
      <h1 className="text-2xl font-bold text-gray-900">Admin Dashboard</h1>
      <p className="text-gray-600">Administrative controls and employee management</p>
    </div>
    <div className="bg-white p-6 rounded-lg shadow">
      <p>Admin dashboard content coming soon...</p>
    </div>
  </div>
);

const EmployeeDashboard: React.FC = () => (
  <div className="space-y-6">
    <div>
      <h1 className="text-2xl font-bold text-gray-900">My Dashboard</h1>
      <p className="text-gray-600">View your attendance and profile information</p>
    </div>
    <div className="bg-white p-6 rounded-lg shadow">
      <p>Employee dashboard content coming soon...</p>
    </div>
  </div>
);

const Unauthorized: React.FC = () => (
  <div className="min-h-screen flex items-center justify-center bg-gray-50">
    <div className="max-w-md w-full text-center">
      <h1 className="text-2xl font-bold text-gray-900 mb-4">Access Denied</h1>
      <p className="text-gray-600 mb-4">You don't have permission to access this page.</p>
      <button
        onClick={() => window.history.back()}
        className="text-primary-600 hover:text-primary-500"
      >
        Go back
      </button>
    </div>
  </div>
);

function App() {
  const { loadUser, isAuthenticated } = useAuthStore();

  useEffect(() => {
    // Load user on app initialization
    loadUser();
  }, [loadUser]);

  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/unauthorized" element={<Unauthorized />} />

          {/* Protected routes with dashboard layout */}
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <DashboardLayout />
              </ProtectedRoute>
            }
          >
            {/* Default redirect based on user role */}
            <Route
              index
              element={
                <Navigate
                  to={
                    isAuthenticated
                      ? useAuthStore.getState().user?.role === UserRole.SUPER_ADMIN
                        ? '/super-admin'
                        : useAuthStore.getState().user?.role === UserRole.ADMIN
                        ? '/admin'
                        : '/employee'
                      : '/login'
                  }
                  replace
                />
              }
            />

            {/* Super Admin routes */}
            <Route
              path="/super-admin"
              element={
                <ProtectedRoute requiredRole={UserRole.SUPER_ADMIN}>
                  <SuperAdminDashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/super-admin/*"
              element={
                <ProtectedRoute requiredRole={UserRole.SUPER_ADMIN}>
                  <SuperAdminDashboard />
                </ProtectedRoute>
              }
            />

            {/* Admin routes */}
            <Route
              path="/admin"
              element={
                <ProtectedRoute requiredRole={UserRole.ADMIN}>
                  <AdminDashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/admin/*"
              element={
                <ProtectedRoute requiredRole={UserRole.ADMIN}>
                  <AdminDashboard />
                </ProtectedRoute>
              }
            />

            {/* Employee routes */}
            <Route
              path="/employee"
              element={
                <ProtectedRoute requiredRole={UserRole.EMPLOYEE}>
                  <EmployeeDashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/employee/*"
              element={
                <ProtectedRoute requiredRole={UserRole.EMPLOYEE}>
                  <EmployeeDashboard />
                </ProtectedRoute>
              }
            />
          </Route>

          {/* Catch all route */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
