#[allow(unused_variables)]

fn main() {

    let x:i8 = i8::MAX;
    let y:i


}


fn type_of<T>(_: &T) -> String{
    format!("{}",std::any::type_name::<T>())

}