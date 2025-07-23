use reqwest;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let url = "https://example.com";
    let body = reqwest::blocking::get(url)?.text()?;
    println!("Fetched {} chars", body.len());
    Ok(())
}
