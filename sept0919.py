#셀레니움을 활용해 인스타그램 포스팅을 크롤링한 데이터를 데이터프레임, 엑셀로 변환 

#인스타그램 로그인 후 시작
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/explore/tags/%EB%9D%BC%EB%A9%B4%EB%A0%88%EC%8B%9C%ED%94%BC/')
word='라면레시피'
url='https://www.instagram.com/explore/tags/'+word
driver.get(url)

#각 포스팅의 본문내용, 태그, 작성시간, 좋아요
ramen_lists=[]
driver.find_elements('css selector','div._aagw')[0].click() 
while True:
    next _pgae= driver.find_elements('css selector', 'div._aaqg._aaqh > button')
    html = driver.page_source 
    soup = BeautifulSoup(html,'html.parser')
    try:
        content = soup.select('h1._aacl._aaco._aacu._aacx._aad7._aade')[0].text #본문
        tags = re.findall('#[a-zA-Zㄱ-ㅎ가-힣]+', content) #태그
        time = soup.select('span > time')[0].text #작성시간
        likes = soup.select(' div > span > a > span > span')[0].text #좋아요
        ramen_lists.append([content, tags, time, likes])
        next_ page[0].click()
    except:
        break

df = pd.DataFrame(ramen_lists, columns=['내용','태그','작성시간','좋아요'])
df.to_excel('ramen_lists',index=False)