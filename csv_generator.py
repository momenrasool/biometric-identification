import os
# Function to rename multiple files
def main():
   file1 = open("./dataset_only_images.csv","a+")
   path="./dataset/punches/"
   classId='1'
   for filename in os.listdir(path):
      file1.writelines(filename+','+classId+'\n')
   file1.close()
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
