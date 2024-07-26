#[allow(unused_variables)]

fn main() {

    let (x,y);

    (x,..) = (1,2);
    [..,y] = [3,4];

    assert_eq!([x,y], [1,4]);


    println!("Success")


}
