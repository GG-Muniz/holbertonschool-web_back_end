export default function updateStudentGradeByCity(list, city, newGrades) {
  if (!Array.isArray(list)) return [];

  const gradesById = new Map(
    (Array.isArray(newGrades) ? newGrades : []).map((g) => [g.studentId, g.grade]),
  );

  return list
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: gradesById.has(student.id) ? gradesById.get(student.id) : 'N/A',
    }));
}
