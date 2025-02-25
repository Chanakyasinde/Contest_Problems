function sortStudents(students){
  // write your code here
  students=students.sort((studentA,studentB) => {
    if (studentA.score === studentB.score) {
        return studentA.name.localeCompare(studentB.name)
    }
    return studentB.score - studentA.score
  })
  return students
}
