public class Figura{
  private double x;
  private double y;

public Figura(double x, double y) {
  System.out.println("Criando figura");
  this.x = x;
  this.y = y;
   }
  
public double getX(){
  return this.x;
}
  
public void setX(){
  this.x = x;
}
  public double getY(){
  return this.y;
}
  
public void setY(){
  this.y = y;
}
  public String desenhar(){
    System.out.println("Desenhando uma figura na posição (" + x + ", " + y + ")");
  }
}
  
