import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

export const getDashboard = () => api.get("dashboard/");
export const getStudents = () => api.get("students/");
export const createStudent = (data) => api.post("students/", data);
export const deleteStudent = (id) => api.delete(`students/${id}/`);

export const getTeachers = () => api.get("teachers/");
export const createTeacher = (data) => api.post("teachers/", data);

export const getCourses = () => api.get("courses/");
export const createCourse = (data) => api.post("courses/", data);

export const getAttendance = () => api.get("attendance/");
export const createAttendance = (data) => api.post("attendance/", data);

export const getRecords = () => api.get("academic-records/");
export const createRecord = (data) => api.post("academic-records/", data);

export default api;
