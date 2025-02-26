function rankStudents(students) {
  students.sort((a, b) => b.score - a.score);

  let rank = 1;
  for (let i = 0; i < students.length; i++) {
    if (i > 0 && students[i].score < students[i - 1].score) {
      rank = i + 1;
    }
    students[i].rank = rank;
  }

  return students;
}
