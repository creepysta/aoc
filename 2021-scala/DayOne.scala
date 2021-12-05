import scala.io.Source._

object DayOne {
  def parse(fileName : String) = {
    val lines = fromFile(fileName).getLines().map(_.toInt).toList
    lines
  }
  def one() : Int = {
    val inp  = parse("DayOne.in")
    val got = inp.foldLeft((inp(0), 0))((b, a) => if(a > b._1) (a, b._2 + 1) else (a, b._2) )
    got._2
  }
  implicit def bool2int(b : Boolean) : Int = if (b) 1 else 0
  def calc(ar : List[Int], got : Int, cnt : Int) : Int = {
    ar match {
      case a :: b :: c :: rest if got == 0 => calc(b :: c :: rest, a + b + c, 0)
      case a :: b :: c :: rest if got > 0 => calc(b :: c :: rest, a + b + c, cnt + (a+b+c > got).toInt)
      case _ => cnt
    }
  }
  def two() : Int = {
    val inp  = parse("DayOne.in2")
    calc(inp, 0, 0)
  }
  def main(args : Array[String]) : Unit = {
    println(one())
    println(two())
  }
}
