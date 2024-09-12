import os
import shutil
import frontmatter

# Define paths
OBSIDIAN_PATH = r'C:\Users\eminm\Desktop\Drive me Google!\Obsidyan\Emin Main' 
QUARTZ_PATH = r'C:\Users\eminm\quartz\content'    # Your Quartz /content folder

def should_publish(note_path):
    # Check if a note has `publish: 1` in its frontmatter
    with open(note_path, 'r', encoding='utf-8') as f:
        try:
            metadata = frontmatter.load(f)
            return metadata.get('publish') == 1
        except Exception as e:
            print(f"Error reading frontmatter from {note_path}: {e}")
            return False
        

        


def sync_notes():
    total_mds = 0
    copied= 0
    skipped= 0
    deleted = 0
    for root, dirs, files in os.walk(OBSIDIAN_PATH):
        for file in files:
            if file.endswith('.md'):
                total_mds += 1
                note_path = os.path.join(root, file)
                if should_publish(note_path):
                    dest_path = os.path.join(QUARTZ_PATH, file)
                    shutil.copy2(note_path, dest_path)  # Copy note to Quartz
                    copied += 1
                    print(f"Published: {note_path} -> {dest_path}")
                else:
                    print(f"Skipped: {note_path}")
                    skipped += 1
    for root, dirs, files in os.walk(QUARTZ_PATH):
        for file in files:
            if file.endswith('.md'):
                note_path = os.path.join(root, file)
                if not should_publish(note_path):
                    os.remove(note_path)
                    deleted += 1
                    print(f"Deleted: {note_path}")
                    
    print(f"total_mds: {total_mds}")
    print(f"copied: {copied}")
    print(f"skipped: {skipped}")
    print(f"deleted: {deleted}")
    
def clean_quartz():
    for root, dirs, files in os.walk(QUARTZ_PATH):
        for file in files:
            if file.endswith('.md'):
                note_path = os.path.join(root, file)
                
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    sync_notes()
