const sortCode: string = `program arraysort💩
var 🔢 arr[6]💩

🚀 📭 bubbleSort() {
    var 🔢 i⬅️0, j⬅️0, temp💩

    🔁 (i ◀️ 5) {
        j ⬅️ 0💩
        🔁 (j ◀️ 5-i) {
            🤔 (arr[j] ▶️ arr[j+1]) {
                temp ⬅️ arr[j]💩
                arr[j] ⬅️ arr[j+1]💩
                arr[j+1] ⬅️ temp💩
            }💩
            j ⬅️ j+1💩
        }
        i ⬅️ i+1💩
    }

}

🚀 void printArr() {
  var 🔢 i ⬅️ 0💩
  🔁 (i ◀️ 6) {
    🖨(arr[i])💩
    i ⬅️ i+1💩
  }
}

main() {
  var 🔢 i ⬅️ 0💩
  arr[0] ⬅️ 7💩
  arr[1] ⬅️ 2💩
  arr[2] ⬅️ 8💩
  arr[3] ⬅️ 1💩
  arr[4] ⬅️ 3💩
  arr[5] ⬅️ 3💩

  🖨(🔤Print unordered array🔤)💩
  printArr()💩

  bubbleSort()💩

  🖨(🔤🔤)💩
  🖨(🔤Print ordered array🔤)💩
  printArr()💩
}`;
export default sortCode;
