import scala.io.Source._

object DayTwo {
  def parse(fileName: String) = {
    val lines = fromFile(fileName).getLines().map(x => x.split(" ")).map(x => (x(0), x(1).toInt)).toList
    lines
  }
  def one() = {
    val inp = parse("DayTwo.in")
    val got = inp.foldLeft( (0, 0) )( (b, a) => a._1 match {
      case "forward" => (b._1 + a._2, b._2)
      case "down" => (b._1, b._2 + a._2)
      case "up" => (b._1, b._2 - a._2)
    }
      )
    got._1 * got._2
  }
  def two() = {
    val inp = parse("DayTwo.in")
    val got = inp.foldLeft( (0, 0, 0) )( (b, a) => a._1 match {
      case "forward" => (b._1 + a._2, b._2 + a._2 * b._3, b._3)
      case "down" => (b._1, b._2 , b._3 + a._2)
      case "up" => (b._1, b._2, b._3 - a._2)
    }
      )
    got._1 * got._2
  }
  def main(args : Array[String]) : Unit = {
    println(one())
    println(two())
  }
}

