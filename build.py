def main():

#Create index.html
    top_template = open('template/top.html').read()

    content = open('content/middle.html').read()

    bottom_template = open('template/bottom.html').read()

    index_html = top_template + content + bottom_template
    open('index.html', 'w+').write(index_html)

#Create contact.html
    contact_top = open('template/top.html').read()

    contact = open('content/contact_middle.html').read()

    contact_bottom = open('template/bottom.html').read()

    contact_html = contact_top + contact + contact_bottom 
    open('contact.html', 'w+').write(contact_html)   

#Create bio.html
    bio_top = open('template/top.html').read()

    bio = open('content/bio_middle.html').read()

    bio_bottom = open('template/bottom.html').read()

    bio_html = bio_top + bio + bio_bottom
    open('bio.html', 'w+').write(bio_html)

#Create resume.html
    resume_top = open('template/top.html').read()

    resume = open('content/resume_middle.html').read()

    resume_bottom = open('template/bottom.html').read()

    resume_html = resume_top + resume + resume_bottom
    open('resume.html', 'w+').write(resume_html)

#invoking the function
main()

if __name__ == "__main__":

    pages = [
{
    'filename': 'content/middle.html',
    'output': 'docs/middle.html',
    'title': 'About me',
},
{
    'filename': 'content/contact_middle.html',
    'output': 'docs/contact_middle.html',
    'title': 'contact',
},
{
    'filename': 'content/bio_middle.html',
    'output': 'bio/bio_middle.html',
    'title': 'bio',
},
{
    'filename': 'content/resume_middle.html',
    'output': 'docs/resume_middle.html',
    'title': 'resume',
},
]

for page in pages:
    
    page_title = page['title']
    print(page_title)
    
# Read in the entire template
    template = open("template/base.html").read()

# Read in the content of the index HTML page
    index_content = open("content/middle.html").read()

# Use the string replace
    finished_index_page = template.replace("{{middle}}", index_content)
    open("docs/index.html", "w+").write(finished_index_page)


