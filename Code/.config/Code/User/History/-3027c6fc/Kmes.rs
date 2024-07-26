#[allow(unused_variables)]

fn main() {

    let (x,y);

    let (x,..) = (1,2);
    let [..,y] = [3,4];

    assert_eq!([x,y], [1,4]);


    println!("Success")


}
