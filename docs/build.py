#Create index.html
top_template = open('../template/top.html').read()

bottom_template = open('../template/bottom.html').read()

content = open('../content/middle.html').read()

index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

#Create contact.html
contact_top = open('../template/contact_top.html').read()
contact_bottom = open('../template/contact_bottom.html').read()

contact = open('../content/contact_middle.html').read()

contact_html = contact_top + contact + contact_bottom 
open('contact.html', 'w+').write(contact_html)   

#Create bio.html
bio_top = open('../template/bio_top.html').read()
bio_bottom = open('../template/bio_bottom.html').read()

bio = open('../content/bio_middle.html').read()

bio_html = bio_top + bio + bio_bottom
open('bio.html', 'w+').write(bio_html)

#Create resume.html

resume_top = open('../template/resume_top.html').read()
resume_bottom = open('../template/resume_bottom.html').read()

resume = open('../content/resume_middle.html').read()

resume_html = resume_top + resume + resume_bottom
open('resume.html', 'w+').write(resume_html)
