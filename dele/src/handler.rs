use dirs::home_dir;
use globset::Glob;
use std::fs::remove_file;
use std::io;
use std::path::{Path, PathBuf};

trait Handler {
  fn delete_file(self, filename: String, file_patterns: Vec<String>) -> io::Result<()>;
}

struct SimpleHandler {
  base_path: PathBuf,
}

impl SimpleHandler {
  fn new(base_dir: String) -> Self {
    let mut base_path = PathBuf::from(base_dir.to_owned());
    if base_dir.starts_with("~") {
      base_path = get_home_dir().to_path_buf();
      base_path.push(Path::new(base_dir.trim_start_matches("~")));
    }
    SimpleHandler { base_path }
  }
}

impl Handler for SimpleHandler {
  fn delete_file(self, filename: String, file_patterns: Vec<String>) -> io::Result<()> {
    for file_pattern in file_patterns {
      let mut path = self.base_path.to_owned();
      path.push(Path::new(file_pattern.as_str()));
      match path.to_str() {
        Some(pattern) => {
          let glob = match Glob::new(pattern) {
            Ok(g) => g.compile_matcher(),
            Err(_) => panic!("failed to create glob pattern"),
          };
          if glob.is_match(filename.as_str()) {
            remove_file(filename.to_owned())?;
          }
        }
        None => panic!("{:?} is not valid path string", path),
      }
    }
    Ok(())
  }
}

fn get_home_dir() -> PathBuf {
  match home_dir() {
    Some(path) => path,
    None => panic!("failed to get home directory"),
  }
}
