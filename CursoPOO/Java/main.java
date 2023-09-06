class Main {

    public static void main(String[] args) {
        System.out.println("Hola Mundo vamos medio medio");
    Car car = new Car("RNY834","AndyRCol");
    car.passegenger = 4;
    car.printDataCar();
    
    Car car2 = new Car();
    car2.driver = "EliverCM";
    car2.license = "AMQ!456";
    car2.passegenger = 4;
    
    car2.printDataCar();
}
}
