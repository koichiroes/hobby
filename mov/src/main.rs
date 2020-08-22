use clap::Clap;
use std::io;
use std::path::PathBuf;
use walkdir::WalkDir;

mod handler;

use handler::{Handler, SimpleHandler};

#[derive(Clap)]
#[clap(version = "1.0", author = "koichiro")]
struct Opts {
    #[clap(short, long)]
    pattern: String,

    #[clap(short, long, parse(from_os_str))]
    dir: PathBuf,
}

fn main() -> io::Result<()> {
    let opts: Opts = Opts::parse();

    let h = SimpleHandler::new(opts.dir.to_owned(), opts.pattern.as_str());
    for entry in WalkDir::new(opts.dir.to_owned()) {
        let entry = match entry {
            Ok(e) => e,
            Err(e) => {
                println!("failed to get directory entry, {}", e);
                continue;
            }
        };
        if entry.file_type().is_dir() {
            let name = entry.path().file_name().unwrap().to_str().unwrap();
            h.move_dir(name)?;
        }
    }
    Ok(())
}
