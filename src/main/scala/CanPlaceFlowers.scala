package leetcode

object CanPlaceFlowers extends App {
  def canPlaceFlowers(flowerbed: Array[Int], n: Int): Boolean = {
    if(flowerbed.isEmpty) false
    else {
      var need = n
      for(i <- 0 until flowerbed.size) {
        if(flowerbed(i) == 0) {
          if(i == 0 && (i+1) < flowerbed.size && flowerbed(i+1) == 0) {
            need -= 1
            flowerbed(i) = 1
          }
          if(flowerbed.size == 1) {
            need -= 1
            flowerbed(i) = 1
          } else if((i - 1) >= 0 && flowerbed(i - 1) == 0){
            if(i == (flowerbed.size - 1)){
              need -= 1
              flowerbed(i) = 1
            }
            else if((i + 1) < flowerbed.size && flowerbed(i + 1) == 0) {
              need -= 1
              flowerbed(i) = 1
            }
          }
        }
      }
      need <= 0
    }
  }

  val arr1 = Array(1,0,0,0,1)
  assert(canPlaceFlowers(arr1, 1))

  val arr2 = Array(1,0,0,0,1)
  assert(canPlaceFlowers(arr2, 2) == false)
}
