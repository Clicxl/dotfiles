#[allow(unused_variables)]

fn main() {

    let x:u8 = 36_u16 as u8;
    assert_eq!("u32".to_string(), type_of(&x));
    println!("Success");


}


fn type_of<T>(_: &T) -> String{
    format!("{}",std::any::type_name::<T>())

}