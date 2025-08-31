export default function getStudentIdsSum(list) {
  if (!Array.isArray(list)) {
    return 0;
  }
  return list.reduce((sum, student) => sum + (Number.isFinite(student.id) ? student.id : 0), 0);
}
