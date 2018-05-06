package leetcode

object MaximumProductThreeNumbers extends App {
  def maximumProduct(nums: Array[Int]): Int = {
     if(nums.size == 3) nums(nums.size - 1) * nums(nums.size - 2) * nums(nums.size - 3)
     else {
        val nums1 = nums.sorted
        val max1 = nums1.last
        val min1 = nums1.head
        if(max1 >=0 && min1 >= 0)  nums1(nums1.size - 1) * nums1(nums1.size - 2) * nums1(nums1.size - 3)
        else if(max1 >= 0 && min1 < 0) {
             val p1 = nums1(0) * nums1(1) * nums1(2)
             val p2 = nums1(0) * nums1(1) * nums1(nums1.size - 3)
             val p3 = nums1(nums1.size - 1) * nums1(nums1.size - 2) * nums1(2)
             val p4 = nums1(nums1.size - 1) * nums1(nums1.size - 2) * nums1(nums1.size - 3)
             val p5 = nums1(0) * nums1(1) * nums1.last
             val p6 = nums1(nums1.size - 1) * nums1(nums1.size - 2) * nums1.head
             p1 max p2 max p3 max p4 max p5 max p6
        } else 0
     }
  }
//  val arr1 = Array(1,2,3,4)
//  println(maximumProduct(arr1))

  //val arr2 = Array(-1,-2,1,2,3)
  //println(maximumProduct(arr2))

  val arr3 = Array(44,46,11,2,12,64,40,60,92,9)
  val arr4 = Array(722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786)//943695360
  val arr5 = Array(-4,-3,-2,-1,60) //720
  println(maximumProduct(arr4))
}
