'''
post_generator.py
Copyright (c) 2019 Copyright Holder All Rights Reserved.
MIT License read the License in base file for more information.
Contact: roshanmis@gmail.com
This script creates posts for your Jekyll blog hosted by Github page.
No plugins required.
'''
import tag_generator
import glob
import datetime

# variable declearation
post_dir = "_posts/"
date = datetime.datetime.now()
post_name = input("Enter Post Name: ")
categories = input("Catagory Of the post: ")

# if I ever updated to something that needed tag I can use this.
# tags = input("Input all tags here separated by space no commas: ")


# formatted the time and file name
formated_date = str(date)[0:10]
new_file_name = post_dir + formated_date + '-' + str(post_name).replace(" ","-") + '.md'

# makes the file if it does not exists
post_file = open(new_file_name, 'a')

# gets the tags and Catagory set up and running
write_str = '---\nlayout: post\ntitle: "' + post_name + '"\ndate: '+ str(date)[0:19] + "+0530"+ '\ncategories: ["'+categories+ '"]  \ntags: '+ tags+ '\ndraft: True\n--- \n' + '\nDummy text - Change it and post your content'

# Post file made
post_file.write(write_str)
post_file.close()

# generate tags
# tag_generator.main()
# print("All good ready! Check the _posts/ folder for the Rmarkdown file. Happy Writing")
