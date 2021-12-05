import scala.io.Source._

object DayThr {
  def parse(fileName: String) = {
    val lines = fromFile(fileName).getLines().toList
    lines
  }
  implicit def bool2int(x : Boolean) : Int = if(x) 1 else 0
  def one() = {
    val inp = parse("DayThr.in")
    def calc(a : List[Int]) : Int = a.foldRight( (1, 0) )( (a, b) => (b._1 * 2, b._2 + a * b._1) )._2
    val got = inp.map(_.split("").map(_.toInt)).foldLeft( List.fill(inp(0).length)(0) )( (b,a) => b.zip(a).map(x => x._1 + x._2) ).map(x => (x > inp.size / 2).toInt)
    val gam = calc(got)
    val eps = calc(got.map(x => (x != 1).toInt))
    gam * eps
  }
  def two() = {

  }
  def main(args : Array[String]) : Unit = {
    println(one())
    println(two())
  }
}


