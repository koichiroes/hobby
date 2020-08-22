use regex::Regex;
use std::fs::{create_dir_all, rename};
use std::io;
use std::path::{Path, PathBuf};

pub(crate) trait Handler {
  fn move_dir(&self, dir_name: &str) -> io::Result<()>;
}

pub(crate) struct SimpleHandler {
  base_path: PathBuf,
  re: Regex,
}

impl SimpleHandler {
  pub fn new(base_path: PathBuf, regex_pattern: &str) -> Self {
    let re = Regex::new(regex_pattern).unwrap();
    SimpleHandler { base_path, re }
  }
}

impl Handler for SimpleHandler {
  fn move_dir(&self, dir_name: &str) -> io::Result<()> {
    if self.re.is_match(dir_name) {
      let cap = self.re.captures(dir_name).unwrap();
      let first_cap = cap.get(1).unwrap().as_str();
      if dir_name == first_cap {
        return Ok(());
      }
      let mut dir_path = self.base_path.to_owned();
      dir_path.push(Path::new(first_cap));
      dir_path.push(Path::new(cap.get(0).unwrap().as_str()));
      match create_dir_all(dir_path.as_path()) {
        Ok(_) => println!("create directory {}", dir_path.display()),
        Err(err) => eprintln!("failed to create directory {}, {}", dir_path.display(), err),
      }
      let mut source_path = self.base_path.to_owned();
      source_path.push(Path::new(dir_name));
      match rename(source_path.as_path(), dir_path.as_path()) {
        Ok(_) => println!(
          "rename directory from {} to {}",
          source_path.display(),
          first_cap
        ),
        Err(err) => eprintln!(
          "failed to rename directory from {} to {}, {}",
          source_path.display(),
          dir_path.display(),
          err
        ),
      }
    }
    Ok(())
  }
}
