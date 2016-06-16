import Chisel._

class greatest_gcd_sum extends Module {
  val io = new Bundle {
    val in_valid = Bool(INPUT)
    val in_number = UInt(INPUT, 6) 
    val out_valid = Bool(OUTPUT)
    val out_indexA = UInt(OUTPUT, 6)
    val out_indexB = UInt(OUTPUT, 6)
    val out_gcd = UInt(OUTPUT, 6)
  }
  io.out_valid := io.in_valid
  io.out_indexA := UInt(0)
  io.out_indexB := UInt(1)
  io.out_gcd := UInt(2)
}


