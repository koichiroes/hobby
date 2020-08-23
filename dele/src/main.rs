use clap::Clap;
use std::io;
use std::path::PathBuf;

mod handler;

use handler::{FSHandler, FileItem, Handler};

#[derive(Clap)]
#[clap(version = "1.0", author = "koichiro")]
struct Opts {
    #[clap(short, long)]
    patterns: Vec<String>,

    #[clap(short, long, parse(from_os_str))]
    dir: PathBuf,
}

fn main() -> io::Result<()> {
    let opts: Opts = Opts::parse();

    let h = FSHandler::new(opts.dir.to_owned(), opts.patterns.to_owned());
    for entry in h.list_files() {
        let name = match entry {
            FileItem::Entry(name) => name,
            FileItem::Err(e) => {
                println!("failed to get directory entry, {}", e);
                continue;
            }
        };
        h.delete_file(name.as_str())?;
    }
    Ok(())
}
