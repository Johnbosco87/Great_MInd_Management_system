import { Routes, Route } from "react-router-dom";

import Layout from "./components/Layout.jsx";

import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import Teachers from "./pages/Teachers";
import Courses from "./pages/Courses";
import Attendance from "./pages/Attendance";
import Records from "./pages/Records";

function App() {
  return (
    <Layout>
      <Routes>

        <Route 
        path="/" 
        element={<Dashboard />}
        />

        <Route
          path="/students"
          element={<Students />}
        />

        <Route
          path="/teachers"
          element={<Teachers />}
        />

        <Route
          path="/courses"
          element={<Courses />}
        />

        <Route
          path="/attendance"
          element={<Attendance />}
        />

        <Route
          path="/records"
          element={<Records />}
        />

      </Routes>
    </Layout>
  );
}

export default App;