horario1=input()
horario2=input()
h1=int(horario1[0:2])
m1=int(horario1[3:5])
s1=int(horario1[6:8])
h2=int(horario2[0:2])
m2=int(horario2[3:5])
s2=int(horario2[6:8])
if h2==h1:
	h3=h2-h1+23
	if m2<m1:
		m3=m2-m1+60
		if s2>s1:
			s3=s2-s1
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2>h1:
	h3=h2-h1
	if m2>=m1:
		m3=m2-m1
		if s2>=s1:
			s3=s2-s1
			print("%02d:%02d:%02d" % (h3,m3,s3))
if h2>h1:
	h3=h2-h1-1
	if m2<m1:
		m3=m2-m1+60
		if s2>s1:
			s3=s2-s1
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2<h1:
	h3=h2-h1+24
	if m2>=m1:
		m3=m2-m1
		if s2>=s1:
			s3=s2-s1
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2>=h1:
	h3=h2-h1-1
	if m2<m1:
		m3=m2-m1+59
		if s2<s1:
			s3=s2-s1+60
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2<h1:
	h3=h2-h1+23
	if m2<m1:
		m3=m2-m1+60
		if s2>=s1:
			s3=s2-s1
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2<h1:
	h3=h2-h1+24
	if m2>=m1:
		m3=m2-m1-1
		if s2<s1:
			s3=s2-s1+60
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2<h1:
	h3=h2-h1+23
	if m2<m1:
		m3=m2-m1+59
		if s2<s1:
			s3=s2-s1+60
			print("%02d:%02d:%02d"% (h3,m3,s3))
if h2>=h1:
	h3=h2-h1
	if m2>=m1:
		m3=m2-m1-1
		if s2<s1:
			s3=s2-s1+60
			print("%02d:%02d:%02d" % (h3,m3,s3))
