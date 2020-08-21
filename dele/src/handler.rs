use globset::{Glob, GlobSet, GlobSetBuilder};
use std::fs::remove_file;
use std::io;
use std::path::{Path, PathBuf};

pub(crate) trait Handler {
  fn delete_file(&self, filename: &str) -> io::Result<()>;
}

pub(crate) struct SimpleHandler {
  set: GlobSet,
}

impl SimpleHandler {
  pub fn new(base_path: PathBuf, patterns: Vec<String>) -> Self {
    let mut builder = GlobSetBuilder::new();
    for pattern in &patterns {
      let mut path = base_path.to_owned();
      path.push(Path::new("**"));
      path.push(Path::new(pattern));
      builder.add(Glob::new(path.to_str().unwrap()).unwrap());
    }
    let set = builder.build().unwrap();
    SimpleHandler { set }
  }
}

impl Handler for SimpleHandler {
  fn delete_file(&self, filename: &str) -> io::Result<()> {
    if self.set.is_match(filename) {
      match remove_file(filename) {
        Ok(_) => println!("{} is deleted", filename),
        Err(e) => println!("failed to delete {}, {}", filename, e),
      }
    }
    Ok(())
  }
}
