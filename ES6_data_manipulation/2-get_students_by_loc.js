export default function getStudentsByLocation(list, city) {
  return Array.isArray(list) ? list.filter((student) => student.location === city) : [];
}
