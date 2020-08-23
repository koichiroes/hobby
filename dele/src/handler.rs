use globset::{Glob, GlobSet, GlobSetBuilder};
use std::fs::remove_file;
use std::io::Result;
use std::iter::Iterator;
use std::path::{Path, PathBuf};
use walkdir::{IntoIter, WalkDir};

pub(crate) enum FileItem {
  Entry(String),
  Err(String),
}

pub(crate) trait Handler {
  fn list_files(&self) -> Box<dyn Iterator<Item = FileItem>>;
  fn delete_file(&self, filename: &str) -> Result<()>;
}

pub(crate) struct FSHandler {
  dir: PathBuf,
  set: GlobSet,
}

impl FSHandler {
  pub fn new(dir: PathBuf, patterns: Vec<String>) -> Self {
    let mut builder = GlobSetBuilder::new();
    for pattern in &patterns {
      let mut path = dir.to_owned();
      path.push(Path::new("**"));
      path.push(Path::new(pattern));
      builder.add(Glob::new(path.to_str().unwrap()).unwrap());
    }
    let set = builder.build().unwrap();
    FSHandler { dir, set }
  }
}

struct FSIterator {
  iter: IntoIter,
}

impl Iterator for FSIterator {
  type Item = FileItem;

  fn next(&mut self) -> Option<FileItem> {
    let ret = match self.iter.next() {
      Some(entry) => entry,
      None => return None,
    };
    let entry = match ret {
      Ok(e) => FileItem::Entry(e.path().display().to_string()),
      Err(e) => FileItem::Err(format!("failed to get next entry, {}", e)),
    };
    Some(entry)
  }
}

impl Handler for FSHandler {
  fn list_files(&self) -> Box<dyn Iterator<Item = FileItem>> {
    Box::new(FSIterator {
      iter: WalkDir::new(self.dir.to_owned()).into_iter(),
    })
  }

  fn delete_file(&self, filename: &str) -> Result<()> {
    if self.set.is_match(filename) {
      match remove_file(filename) {
        Ok(_) => println!("{} is deleted", filename),
        Err(e) => println!("failed to delete {}, {}", filename, e),
      }
    }
    Ok(())
  }
}
