
-- 테이블 생성
CREATE TABLE IF NOT EXISTS emotion (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT '기타',
    description TEXT NOT NULL,
    example TEXT
);
INSERT INTO emotion (title, category, description, example)
VALUES
UPDATE emotion
SET example='밤길을 혼자 걷고 있는데 뒤에서 발소리가 들려 겁났다.'
WHERE title='겁나다'
;
UPDATE emotion
SET example='갑작스러운 지진 소식에 공포스러운 느낌이 들었다.'
WHERE title='공포스럽다'
;
UPDATE emotion
SET example='전쟁이 발발할 것 같은 급박한 상황이었다.'
WHERE title='급박하다'
;
UPDATE emotion
SET example='회의실의 분위기는 중요한 발표를 앞두고 점점 더 긴박해졌다.'
WHERE title='긴박하다'
;
UPDATE emotion
SET example='면접 시간이 다가오자 점점 긴장되었다.'
WHERE title='긴장되다'
;
UPDATE emotion
SET example='영화 속 장면이 너무 끔찍해서 눈을 감았다.'
WHERE title='끔찍하다'
;
UPDATE emotion
SET example='처음 가본 도시는 모든 것이 낯설게 느껴졌다.'
WHERE title='낯설다'
;
UPDATE emotion
SET example='병원에 간 친구를 기다리며 노심초사했다.'
WHERE title='노심초사하다'
;
UPDATE emotion
SET example='중요한 발표를 앞두고 두려운 마음이 커져갔다.'
WHERE title='두렵다'
;
UPDATE emotion
SET example='끔찍한 사고 소식을 듣고 몸서리쳤다.'
WHERE title='몸서리치다'
;
UPDATE emotion
SET example='밤에 들리는 바람 소리가 너무 무서웠다.'
WHERE title='무섭다'
;
UPDATE emotion
SET example='폐가에 들어갔을 때 무시무시한 기운이 느껴졌다.'
WHERE title='무시무시하다'
;
UPDATE emotion
SET example='중요한 발표를 앞두고 그녀의 마음은 불안정했다.'
WHERE title='불안정하다'
;
UPDATE emotion
SET example='시험 결과가 나오기 전까지 마음이 불안했다.'
WHERE title='불안하다'
;
UPDATE emotion
SET example='그 사람의 말투는 살벌해서 다가가기 어려웠다.'
WHERE title='살벌하다'
;
UPDATE emotion
SET example='귀신을 보고 놀라서 얼굴이 새파래졌다.'
WHERE title='새파래지다'
;
UPDATE emotion
SET example='뒤에서 누군가 따라오는 기분이 들어서 섬뜩했다.'
WHERE title='섬뜩하다'
;
UPDATE emotion
SET example='갑자기 들린 비명 소리에 소름이 끼쳤다.'
WHERE title='소름끼치다'
;
UPDATE emotion
SET example='바람이 불어오는 저녁 거리의 분위기가 스산했다.'
WHERE title='스산하다'
;
UPDATE emotion
SET example='높은 곳에 올라가니 아슬아슬한 기분이 들었다.'
WHERE title='아슬아슬하다'
;
UPDATE emotion
SET example='높은 곳에서 아래를 내려다보니 순간적으로 아찔함을 느꼈다.'
WHERE title='아찔하다'
;
UPDATE emotion
SET example='중요한 시험 결과를 기다리며 안절부절못했다.'
WHERE title='안절부절못하다'
;
UPDATE emotion
SET example='어두운 골목길에서 갑자기 누군가 나타나 오싹함을 느꼈다.'
WHERE title='오싹하다'
;
UPDATE emotion
SET example='겨울밤의 으스스한 바람 소리에 잠을 이루지 못했다.'
WHERE title='으스스하다'
;
UPDATE emotion
SET example='을씨년스러운 날씨에 괜히 기분이 처지는 것 같았다.'
WHERE title='을씨년스럽다'
;
UPDATE emotion
SET example='영화 속 악당의 잔인한 행동에 눈살이 찌푸려졌다.'
WHERE title='잔인하다'
;
UPDATE emotion
SET example='잔혹한 범죄 소식을 듣고 마음이 무거워졌다.'
WHERE title='잔혹하다'
;
UPDATE emotion
SET example='면접 결과를 기다리며 하루 종일 조마조마했다.'
WHERE title='조마조마하다'
;
UPDATE emotion
SET example='프로젝트가 순조롭게 진행되는데도, 그는 사소한 문제에 조바심했다.'
WHERE title='조바심하다'
;
UPDATE emotion
SET example='갑작스러운 큰 소리에 질겁하여 몸이 움츠러들었다.'
WHERE title='질겁하다'
;
UPDATE emotion
SET example='기차 시간이 다가오는데 늦을까 봐 초조했다.'
WHERE title='초조하다'
;
UPDATE emotion
SET example='오늘 해야 할 일을 모두 끝내고 나니 마음이 가벼웠다.'
WHERE title='가볍다'
;
UPDATE emotion
SET example='아침 운동을 마치고 나니 몸이 가뿐해졌다.'
WHERE title='가뿐하다'
;
UPDATE emotion
SET example='졸업식에서 가족과 함께한 순간이 감개무량했다.'
WHERE title='감개무량하다'
;
UPDATE emotion
SET example='오랜만에 만난 친구의 따뜻한 환영에 감격했다.'
WHERE title='감격하다'
;
UPDATE emotion
SET example='선생님의 진심 어린 말씀에 깊이 감동했다.'
WHERE title='감동하다'
;
UPDATE emotion
SET example='그 영화는 내 인생에 있어 감명깊은 작품이었다.'
WHERE title='감명깊다'
;
UPDATE emotion
SET example='감미로운 음악 소리에 마음이 편안해졌다.'
WHERE title='감미롭다'
;
UPDATE emotion
SET example='부모님의 희생과 사랑에 감복했다.'
WHERE title='감복하다'
;
UPDATE emotion
SET example='도움을 준 친구에게 진심으로 감사했다.'
WHERE title='감사하다'
;
UPDATE emotion
SET example='오랜만에 졸업 앨범을 보니 학창 시절의 추억이 감회롭게 다가왔다.'
WHERE title='감회롭다'
;
UPDATE emotion
SET example='바람에 흔들리는 갈대밭은 자연의 아름다움을 정감하게 느끼게 한다.'
WHERE title='정감하다'
;
UPDATE emotion
SET example='봄바람을 맞으며 공원을 산책하니 기분이 경쾌했다.'
WHERE title='경쾌하다'
;
UPDATE emotion
SET example='친구가 내 생일을 기억하고 선물을 준비해줘서 정말 고마웠다.'
WHERE title='고맙다'
;
UPDATE emotion
SET example='새로운 프로젝트에 참여하게 되어 의욕이 고취되었다.'
WHERE title='고취되다'
;
UPDATE emotion
SET example='저녁 노을이 지는 바닷가 경치가 정말 근사했다.'
WHERE title='근사하다'
;
UPDATE emotion
SET example='오늘 저녁에 상쾌한 바람을 맞으며 퇴근하니 기분이 좋았다.'
WHERE title='기분 좋다'
;
UPDATE emotion
SET example='오랜만에 친구를 만나 즐거운 시간을 보낼 수 있어 기뻤다.'
WHERE title='기쁘다'
;
UPDATE emotion
SET example='별이 빛나는 하늘 아래에서 산책하니 분위기가 낭만적이었다.'
WHERE title='낭만적이다'
;
UPDATE emotion
SET example='오래 기다리던 소포가 도착해서 정말 달가웠다.'
WHERE title='달갑다'
;
UPDATE emotion
SET example='동생이 스스로 숙제를 다 마친 모습을 보니 대견했다.'
WHERE title='대견하다'
;
UPDATE emotion
SET example='첫 데이트를 앞두고 마음이 두근거렸다.'
WHERE title='두근거리다'
;
UPDATE emotion
SET example='친구가 내 고민을 들어주고 위로해줘서 마음이 따뜻해졌다.'
WHERE title='따뜻하다'
;
UPDATE emotion
SET example='겨울 아침에 따스한 햇살이 창문으로 들어와 마음이 포근해졌다.'
WHERE title='따스하다'
;
UPDATE emotion
SET example='모든 준비를 끝내고 결과가 잘 나와서 만족했다.'
WHERE title='만족하다'
;
UPDATE emotion
SET example='그의 미소는 정말 매력적이어서 눈을 뗄 수 없었다.'
WHERE title='매력적이다'
;
UPDATE emotion
SET example='오랜만에 만난 친구와 반갑게 인사를 나눴다.'
WHERE title='반갑다'
;
UPDATE emotion
SET example='가을 산의 단풍은 정말 보기 좋았다.'
WHERE title='보기 좋다'
;
UPDATE emotion
SET example='열심히 준비한 발표가 성공적으로 끝나서 뿌듯했다.'
WHERE title='뿌듯하다'
;
UPDATE emotion
SET example='아기가 웃으며 나를 바라보는 모습이 정말 사랑스러웠다.'
WHERE title='사랑스럽다'
;
UPDATE emotion
SET example='발표를 앞두고 상기되어 얼굴이 붉어졌다.'
WHERE title='상기되다'
;
UPDATE emotion
SET example='아침 공기를 마시니 기분이 상쾌했다.'
WHERE title='상쾌하다'
;
UPDATE emotion
SET example='레몬의 상큼한 향기가 코끝을 자극했다.'
WHERE title='상큼하다'
;
UPDATE emotion
SET example='여행을 앞두고 설레는 마음을 감출 수 없었다.'
WHERE title='설레다'
;
UPDATE emotion
SET example='밀린 일을 모두 끝내고 나니 속이 시원하다.'
WHERE title='속 시원하다'
;
UPDATE emotion
SET example='놀이공원에 와서 신나게 놀았다.'
WHERE title='신나다'
;
UPDATE emotion
SET example='축제에서 춤을 추며 신명나게 즐겼다.'
WHERE title='신명나다'
;
UPDATE emotion
SET example='친구들과 여행 계획을 세우니 신바람이 났다.'
WHERE title='신바람 나다'
;
UPDATE emotion
SET example='새로운 아이디어가 신선하게 다가왔다.'
WHERE title='신선하다'
;
UPDATE emotion
SET example='오랜만에 만난 친구를 보니 싱글벙글하게 웃었다.'
WHERE title='싱글벙글하다'
;
UPDATE emotion
SET example='칭찬을 받으니 쑥스러워 얼굴이 빨개졌다.'
WHERE title='쑥스럽다'
;
UPDATE emotion
SET example='장난스러운 농담에 입꼬리가 씰룩거렸다.'
WHERE title='씰룩거리다'
;
UPDATE emotion
SET example='아이들의 어여쁜 미소에 마음이 따뜻해졌다.'
WHERE title='어여쁘다'
;
UPDATE emotion
SET example='정원에 핀 꽃들이 예뻐서 사진을 찍었다.'
WHERE title='예쁘다'
;
UPDATE emotion
SET example='그녀의 무도회 드레스는 정말 우아했다.'
WHERE title='우아하다'
;
UPDATE emotion
SET example='친구의 농담에 크게 웃었다.'
WHERE title='웃다'
;
UPDATE emotion
SET example='실수를 하고도 그냥 웃어넘겼다.'
WHERE title='웃어넘기다'
;
UPDATE emotion
SET example='파티에서 유쾌한 시간을 보냈다.'
WHERE title='유쾌하다'
;
UPDATE emotion
SET example='선생님께 칭찬을 받고 어깨가 으쓱했다.'
WHERE title='으쓱하다'
;
UPDATE emotion
SET example='형은 자신의 농구 실력을 자부하고 있었다'
WHERE title='자부하다'
;
UPDATE emotion
SET example='친구들과 놀이공원에 가서 롤러코스터를 타니 정말 재미있었다.'
WHERE title='재미있다'
;
UPDATE emotion
SET example='나는 지금 기분이 최고로 좋다.'
WHERE title='좋다'
;
UPDATE emotion
SET example='오랜만에 친구들과 만나 수다를 떨며 시간을 보내니 정말 즐거웠다.'
WHERE title='즐겁다'
;
UPDATE emotion
SET example='길을 건너다 넘어졌는데 차가 오지 않아서 천만다행이었다.'
WHERE title='천만다행이다'
;
UPDATE emotion
SET example='오랜 친구를 만나면 항상 친근한 느낌이 들어 기분이 좋다.'
WHERE title='친근하다'
;
UPDATE emotion
SET example='이 동네는 어릴 적 자주 놀러 와서 그런지 항상 친숙하게 느껴진다.'
WHERE title='친숙하다'
;
UPDATE emotion
SET example='첫 데이트라 그런지 설레서 심장이 콩닥거렸다.'
WHERE title='콩닥거리다'
;
UPDATE emotion
SET example='깨끗하고 정돈된 방에 들어가니 기분이 쾌적했다.'
WHERE title='쾌적하다'
;
UPDATE emotion
SET example='열심히 준비한 발표가 성공적으로 끝나서 정말 통쾌했다.'
WHERE title='통쾌하다'
;
UPDATE emotion
SET example='따뜻한 차 한 잔을 마시고 나니 마음이 편안해졌다.'
WHERE title='편안하다'
;
UPDATE emotion
SET example='사랑하는 사람들과 함께 시간을 보내는 순간이 가장 행복하다.'
WHERE title='행복하다'
;
UPDATE emotion
SET example='오랫동안 고민하던 일을 다 해결하고 나니 속이 후련하다.'
WHERE title='후련하다'
;
UPDATE emotion
SET example='그의 연주는 정말 훌륭해서 감동적이었다.'
WHERE title='훌륭하다'
;
UPDATE emotion
SET example='아이들이 연극에서 멋지게 연기를 해내는 모습을 보니 정말 흐뭇했다.'
WHERE title='흐뭇하다'
;
UPDATE emotion
SET example='오랜만에 맛있는 음식을 배불리 먹고 나니 흡족한 마음이 들었다.'
WHERE title='흡족하다'
;
UPDATE emotion
SET example='음악을 들으며 춤을 추니 몸도 마음도 흥겹다.'
WHERE title='흥겹다'
;
UPDATE emotion
SET example='로또에 당첨된 친구가 희희낙락하며 기쁨을 감추지 못했다.'
WHERE title='희희낙락하다'
;
UPDATE emotion
SET example='친구가 내 농담에 히죽거리며 웃어주었다.'
WHERE title='히죽거리다'
;
UPDATE emotion
SET example='아침에 일어났는데 뭔가 개운찮아서 하루 종일 기운이 없었다.'
WHERE title='개운찮다'
;
UPDATE emotion
SET example='그는 그의 실수가 겸연쩍은지 씩 멋쩍은 웃음을 보였다.'
WHERE title='겸연쩍다'
;
UPDATE emotion
SET example='갑자기 이름이 불려서 여러 사람 앞에 서니 계면쩍었다.'
WHERE title='계면쩍다'
;
UPDATE emotion
SET example='친구가 돈을 빌려달라고 해서 정말 곤란했다.'
WHERE title='곤란하다'
;
UPDATE emotion
SET example='프로젝트가 성공적으로 끝나서 기고만장한 기분이었다.'
WHERE title='기고만장하다'
;
UPDATE emotion
SET example='칭찬을 받을 때마다 나는 낯간지럽다.'
WHERE title='낯간지럽다'
;
UPDATE emotion
SET example='부끄러운 실수를 해서 모두 앞에서 낯뜨거웠다.'
WHERE title='낯뜨겁다'
;
UPDATE emotion
SET example='아이가 늦게 들어오니 노파심이 들어 잠을 못 이뤘다.'
WHERE title='노파심이 들다'
;
UPDATE emotion
SET example='농담이 통하지 않아 머쓱해졌다.'
WHERE title='머쓱하다'
;
UPDATE emotion
SET example='혼자 큰 소리로 웃었는데 아무도 반응이 없어서 멋쩍었다.'
WHERE title='멋쩍다'
;
UPDATE emotion
SET example='친구가 내 비밀을 모두 앞에서 말해서 무안했다.'
WHERE title='무안하다'
;
UPDATE emotion
SET example='어른들 앞에서 아이처럼 떼를 쓰는 동생을 보니 민망했다.'
WHERE title='민망하다'
;
UPDATE emotion
SET example='내가 한 말이 너무 유치해서 몸이 오그라들었다.'
WHERE title='오그라들다'
;
UPDATE emotion
SET example='처음 보는 사람들 앞에서 쭈뼛거리며 인사를 했다.'
WHERE title='쭈뼛거리다'
;
UPDATE emotion
SET example='그의 그림 실력에 감탄할 수밖에 없었다.'
WHERE title='감탄하다'
;
UPDATE emotion
SET example='갑작스럽게 내린 비에 우산도 없이 젖고 말았다.'
WHERE title='갑작스럽다'
;
UPDATE emotion
SET example='그의 충격적인 소식을 듣고 경악했다.'
WHERE title='경악하다'
;
UPDATE emotion
SET example='갓 태어난 아기의 작은 손과 발을 보니 생명의 신비로움에 경이로움을 느꼈다.'
WHERE title='경이롭다'
;
UPDATE emotion
SET example='갑작스러운 질문에 곤혹스러워졌다.'
WHERE title='곤혹스럽다'
;
UPDATE emotion
SET example='급작스럽게 결정된 회의 일정에 모두 당황했다.'
WHERE title='급작스럽다'
;
UPDATE emotion
SET example='갑자기 나타난 벌레 때문에 기겁했다.'
WHERE title='기겁하다'
;
UPDATE emotion
SET example='그의 변명에 기막혀서 말이 나오지 않았다.'
WHERE title='기막히다'
;
UPDATE emotion
SET example='집 앞에 갑자기 나타난 고양이가 나를 뚫어져라 쳐다보는 모습이 기묘했다.'
WHERE title='기묘하다'
;
UPDATE emotion
SET example='친구가 갑자기 외계인을 만난 이야기를 해서 기상천외하다는 생각이 들었다.'
WHERE title='기상천외하다'
;
UPDATE emotion
SET example='길을 걷다가 기이한 모양의 구름을 보고 잠시 멈춰 섰다.'
WHERE title='기이하다'
;
UPDATE emotion
SET example='친구가 복권에 당첨되었다는 소식을 듣고 기절초풍할 뻔했다.'
WHERE title='기절초풍하다'
;
UPDATE emotion
SET example='너무 무서운 영화를 보고 기절할 뻔했다.'
WHERE title='기절하다'
;
UPDATE emotion
SET example='갑작스런 큰 소리에 놀라서 까무러칠 뻔했다.'
WHERE title='까무러치다'
;
UPDATE emotion
SET example='두 친구가 싸우고 있어서 난감한 상황에 처했다.'
WHERE title='난감하다'
;
UPDATE emotion
SET example='그녀의 피아노 연주 실력은 정말 놀라웠다.'
WHERE title='놀랍다'
;
UPDATE emotion
SET example='갑자기 상사가 나에게 중요한 발표를 맡기겠다고 해서 당혹했다.'
WHERE title='당혹하다'
;
UPDATE emotion
SET example='길을 잃어버려서 당황하고 말았다.'
WHERE title='당황하다'
;
UPDATE emotion
SET example='뒤에서 누군가 내 이름을 부르는 소리에 뜨끔했다.'
WHERE title='뜨금하다'
;
UPDATE emotion
SET example='친구가 내가 싫어하는 음식을 권해서 뜨악했다.'
WHERE title='뜨악하다'
;
UPDATE emotion
SET example='이번 프로젝트의 규모가 만만찮아 보였다.'
WHERE title='만만찮다'
;
UPDATE emotion
SET example='뉴스에서 들은 사건이 너무 쇼킹해서 말을 잇지 못했다.'
WHERE title='쇼킹하다'
;
UPDATE emotion
SET example='예상치 못한 결과에 아연실색하고 말았다.'
WHERE title='아연실색하다'
;
UPDATE emotion
SET example='새로운 환경에 적응하지 못해 어리둥절했다.'
WHERE title='어리둥절하다'
;
UPDATE emotion
SET example='복권에 당첨되었다는 사실에 아직 얼떨떨하다.'
WHERE title='얼떨떨하다'
;
UPDATE emotion
SET example='뒤에서 누가 나를 부르자 깜짝 놀라서 움찔했다.'
WHERE title='움찔하다'
;
UPDATE emotion
SET example='평소와 다른 그의 행동이 이상하게 느껴졌다.'
WHERE title='이상하다'
;
UPDATE emotion
SET example='어두운 골목길을 걸을 때마다 전율이 느껴진다.'
WHERE title='전율하다'
;
UPDATE emotion
SET example='친구의 교통사고 소식을 듣고 가슴이 철렁했다.'
WHERE title='철렁하다'
;
UPDATE emotion
SET example='내가 믿었던 사람이 나를 배신했다는 소식은 정말 충격적이었다.'
WHERE title='충격적이다'
;
UPDATE emotion
SET example='친구가 로또에 당첨되었다는 말을 듣고 휘둥그레졌다.'
WHERE title='휘둥그레지다'
;
UPDATE emotion
SET example='갑자기 뒤에서 누군가가 부르는 소리에 흠칫했다.'
WHERE title='흠칫하다'
;
UPDATE emotion
SET example='그런 가당찮은 요구를 하다니 정말 어이가 없었다.'
WHERE title='가당찮다'
;
UPDATE emotion
SET example='매번 거짓말로 나를 속이려는 모습이 가증스러웠다.'
WHERE title='가증스럽다'
;
UPDATE emotion
SET example='그날의 날씨는 정말 거지같아서 하루 종일 기분이 나빴다.'
WHERE title='거지같다'
;
UPDATE emotion
SET example='친구의 배신에 격노하여 한동안 말을 잃었다.'
WHERE title='격노하다'
;
UPDATE emotion
SET example='부당한 대우에 격분하여 항의했다.'
WHERE title='격분하다'
;
UPDATE emotion
SET example='그의 연설에 많은 사람들이 격앙되기 시작했다.'
WHERE title='격앙되다'
;
UPDATE emotion
SET example='논쟁이 격양되어 서로의 목소리가 점점 커졌다.'
WHERE title='격양되다'
;
UPDATE emotion
SET example='시위 현장의 분위기가 점점 격해졌다.'
WHERE title='격해지다'
;
UPDATE emotion
SET example='나를 속이려던 친구의 행동이 정말 괘씸했다.'
WHERE title='괘씸하다'
;
UPDATE emotion
SET example='많은 사람들 앞에서 실수를 하고 나니 굴욕감이 들었다.'
WHERE title='굴욕감 들다'
;
UPDATE emotion
SET example='동료의 무례한 말에 기분이 나빠졌다.'
WHERE title='기분 나쁘다'
;
UPDATE emotion
SET example='그의 무례한 태도에 나는 노여워했다.'
WHERE title='노여워하다'
;
UPDATE emotion
SET example='회사에서 무시당하는 느낌이 들어 모멸감을 느꼈다.'
WHERE title='모멸감 들다'
;
UPDATE emotion
SET example='회의 중에 나를 지적하는 동료의 말이 모욕적이었다.'
WHERE title='모욕적이다'
;
UPDATE emotion
SET example='아이들이 서로 못되게 구는 것을 보고 화가 났다.'
WHERE title='못되다'
;
UPDATE emotion
SET example='그의 행동이 마음에 들지 않아 못마땅했다.'
WHERE title='못마땅하다'
;
UPDATE emotion
SET example='회사에서 내 의견을 무시당했을 때 정말 화가 치밀었다.'
WHERE title='무시당하다'
;
UPDATE emotion
SET example='친구가 내 비밀을 다른 사람들에게 말한 게 너무 밉다.'
WHERE title='밉다'
;
UPDATE emotion
SET example='아이가 부모님께 발칙한 말을 해서 모두가 놀랐다.'
WHERE title='발칙하다'
;
UPDATE emotion
SET example='그 사람에게 받은 상처 때문에 복수심이 들었다.'
WHERE title='복수심 들다'
;
UPDATE emotion
SET example='부당한 대우를 받았을 때 분개하지 않을 수 없었다.'
WHERE title='분개하다'
;
UPDATE emotion
SET example='그가 나에게 거짓말을 했다는 걸 알았을 때 분노했다.'
WHERE title='분노하다'
;
UPDATE emotion
SET example='억울한 상황에 처하니 분통이 터졌다.'
WHERE title='분통터지다'
;
UPDATE emotion
SET example='승리할 수 있었던 경기에서 패해서 정말 분했다.'
WHERE title='분하다'
;
UPDATE emotion
SET example='새로 산 가전제품이 기대에 못 미쳐 불만스럽다.'
WHERE title='불만스럽다'
;
UPDATE emotion
SET example='서비스의 질이 기대 이하라서 불만족했다.'
WHERE title='불만족하다'
;
UPDATE emotion
SET example='그와의 대화가 너무 불유쾌해서 빨리 끝내고 싶었다.'
WHERE title='불유쾌하다'
;
UPDATE emotion
SET example='그는 항상 비딱한 태도로 사람들을 대한다.'
WHERE title='비딱하다'
;
UPDATE emotion
SET example='친구가 내 실수를 비아냥거리며 놀렸다.'
WHERE title='비아냥거리다'
;
UPDATE emotion
SET example='그는 다른 사람의 의견을 빈정거리며 무시한다.'
WHERE title='빈정거리다'
;
UPDATE emotion
SET example='작은 일에 삐쳐서 뾰루퉁해진 아이가 귀엽다.'
WHERE title='뾰루퉁하다'
;
UPDATE emotion
SET example='사소한 말 한마디에 삐쳐서 며칠 동안 말을 안 했다.'
WHERE title='삐치다'
;
UPDATE emotion
SET example='자꾸만 틀리는 시험 점수가 내 속을 썩인다.'
WHERE title='속썩이다'
;
UPDATE emotion
SET example='공공장소에서 넘어져서 정말 수치스러웠다.'
WHERE title='수치스럽다'
;
UPDATE emotion
SET example='반복되는 실수에 신경질이 났다.'
WHERE title='신경질나다'
;
UPDATE emotion
SET example='그는 심술궂게 다른 사람의 실수를 즐기곤 한다.'
WHERE title='심술궂다'
;
UPDATE emotion
SET example='아침부터 친구가 나를 계속 놀려서 심통이 나고 말았다.'
WHERE title='심통나다'
;
UPDATE emotion
SET example='운동을 마치고 나서 숨이 차서 씩씩거리며 물을 마셨다.'
WHERE title='씩씩거리다'
;
UPDATE emotion
SET example='그가 나를 비웃을 때마다 아니꼽다는 생각이 들었다.'
WHERE title='아니꼽다'
;
UPDATE emotion
SET example='도움을 요청했지만 그는 야박하게도 거절했다.'
WHERE title='야박하다'
;
UPDATE emotion
SET example='그가 뒤에서 나를 험담할 때 그의 야비한 행동에 실망했다.'
WHERE title='야비하다'
;
UPDATE emotion
SET example='친구가 나보다 시험 점수가 높을 때 약이 올라 잠을 이룰 수 없었다.'
WHERE title='약오르다'
;
UPDATE emotion
SET example='동생이 내 앞에서 일부러 자랑할 때마다 얄밉기 그지없다.'
WHERE title='얄밉다'
;
UPDATE emotion
SET example='갑자기 일이 이렇게 될 줄은 몰라서 정말 어이없었다.'
WHERE title='어이없다'
;
UPDATE emotion
SET example='아침부터 비가 쏟아져서 약속이 취소되어 언짢은 기분이었다.'
WHERE title='언짢다'
;
UPDATE emotion
SET example='그의 무례한 행동 때문에 울화통이 터질 것 같았다.'
WHERE title='울화통 터지다'
;
UPDATE emotion
SET example='그가 나를 배신했을 때 한동안 그를 원망하지 않을 수 없었다.'
WHERE title='원망하다'
;
UPDATE emotion
SET example='그의 말을 듣고 나니 뭔가 의심스러운 점이 많아졌다.'
WHERE title='의심스럽다'
;
UPDATE emotion
SET example='그가 나에게 했던 거짓말들 때문에 그를 증오하게 되었다.'
WHERE title='증오하다'
;
UPDATE emotion
SET example='부당한 대우를 받을 때마다 진노하지 않을 수 없었다.'
WHERE title='진노하다'
;
UPDATE emotion
SET example='친구가 다른 친구와 더 친하게 지내는 것을 보고 질투가 났다.'
WHERE title='질투하다'
;
UPDATE emotion
SET example='교통 체증 때문에 오랫동안 차 안에 갇혀 있어 짜증이 났다.'
WHERE title='짜증나다'
;
UPDATE emotion
SET example='그의 배신을 떠올릴 때마다 치가 떨렸다.'
WHERE title='치가 떨리다'
;
UPDATE emotion
SET example='상사의 부당한 지시에 화가 치밀어 올랐다.'
WHERE title='치밀어오르다'
;
UPDATE emotion
SET example='모두가 지켜보는 앞에서 넘어지는 것은 정말 치욕적이었다.'
WHERE title='치욕적이다'
;
UPDATE emotion
SET example='좋은 소식을 듣고 너무 흥분해서 잠을 이루지 못했다.'
WHERE title='흥분하다'
;
UPDATE emotion
SET example='길 잃은 강아지가 비를 맞으며 떨고 있는 모습을 보니 가련한 마음이 들었다.'
WHERE title='가련하다'
;
UPDATE emotion
SET example='이별의 순간에 그녀의 눈물을 보니 가슴 아팠다.'
WHERE title='가슴 아프다'
;
UPDATE emotion
SET example='지팡이를 짚고 혼자 길을 걷는 할머니의 모습이 가엾게 느껴졌다.'
WHERE title='가엾다'
;
UPDATE emotion
SET example='그의 실수에 대한 처벌은 너무 가혹하다고 생각했다.'
WHERE title='가혹하다'
;
UPDATE emotion
SET example='도시의 삶은 각박하게 느껴져서 가끔은 따뜻한 시골이 그립다.'
WHERE title='각박하다'
;
UPDATE emotion
SET example='간절한 마음으로 시험 결과를 기다리고 있다.'
WHERE title='간절하다'
;
UPDATE emotion
SET example='부모님은 내가 늦게 들어올 때마다 걱정하신다.'
WHERE title='걱정하다'
;
UPDATE emotion
SET example='하루 종일 일하고 집에 돌아오니 몸이 고달팠다.'
WHERE title='고달프다'
;
UPDATE emotion
SET example='혼자 남겨진 집에서 고독함을 느꼈다.'
WHERE title='고독하다'
;
UPDATE emotion
SET example='모두의 앞에서 실수를 저질러서 곤욕스러웠다.'
WHERE title='곤욕스럽다'
;
UPDATE emotion
SET example='친구가 떠난 후 방이 공허하게 느껴졌다.'
WHERE title='공허하다'
;
UPDATE emotion
SET example='그의 말 한마디에 마음이 괴로웠다.'
WHERE title='괴롭다'
;
UPDATE emotion
SET example='비 오는 날 들려오는 피아노 소리가 구슬프게 들렸다.'
WHERE title='구슬프다'
;
UPDATE emotion
SET example='오랜만에 고향을 떠올리니 그리운 마음이 가득하다.'
WHERE title='그리워하다'
;
UPDATE emotion
SET example='내일 있을 중요한 발표 때문에 근심스러운 마음이 가시질 않는다.'
WHERE title='근심스럽다'
;
UPDATE emotion
SET example='영화를 보던 중 감동적인 장면에서 글썽글썽했다.'
WHERE title='글썽글썽하다'
;
UPDATE emotion
SET example='그의 인생 이야기를 들으며 기구한 삶을 살았음을 느꼈다.'
WHERE title='기구하다'
;
UPDATE emotion
SET example='감기에 걸려서 하루 종일 기운 없이 누워 있었다.'
WHERE title='기운 없다'
;
UPDATE emotion
SET example='심혈을 기울인 프로젝트가 실패로 끝나 낙담했다.'
WHERE title='낙담하다'
;
UPDATE emotion
SET example='꿈꾸던 대학에 떨어지자 낙망한 마음을 감출 수가 없었다.'
WHERE title='낙망하다'
;
UPDATE emotion
SET example='바라던 일이 이루어지지 않아서 한동안 낙심하고 있었다.'
WHERE title='낙심하다'
;
UPDATE emotion
SET example='친구의 부탁을 거절할 수 없어서 참 난처했다.'
WHERE title='난처하다'
;
UPDATE emotion
SET example='친구가 새로 산 차를 보니 정말 남부러웠다.'
WHERE title='남부럽다'
;
UPDATE emotion
SET example='여행 가방을 집에 두고 오는 바람에 낭패스러웠다.'
WHERE title='낭패스럽다'
;
UPDATE emotion
SET example='그의 냉혹한 말에 상처를 받아 마음이 아팠다.'
WHERE title='냉혹하다'
;
UPDATE emotion
SET example='할머니의 손편지를 읽으니 눈물겨워 눈물이 났다.'
WHERE title='눈물겹다'
;
UPDATE emotion
SET example='중요한 시험 결과를 기다리느라 마음이 뒤숭숭했다.'
WHERE title='뒤숭숭하다'
;
UPDATE emotion
SET example='끝없이 펼쳐진 사막을 보니 망막한 기분이 들었다.'
WHERE title='망막하다'
;
UPDATE emotion
SET example='갑작스러운 소식에 망연자실하여 아무 말도 할 수 없었다.'
WHERE title='망연자실하다'
;
UPDATE emotion
SET example='친구의 이별 소식을 듣고 먹먹해지는 기분이었다.'
WHERE title='먹먹하다'
;
UPDATE emotion
SET example='오랜만에 가족들과 함께한 저녁 식사에 뭉클한 감정이 들었다.'
WHERE title='뭉클하다'
;
UPDATE emotion
SET example='친구에게 약속을 지키지 못해 미안한 마음이 든다.'
WHERE title='미안하다'
;
UPDATE emotion
SET example='졸업식에서 부모님의 얼굴을 보니 감정이 복받쳐 올랐다.'
WHERE title='복받치다'
;
UPDATE emotion
SET example='많은 사람들 앞에서 실수하여 부끄러웠다.'
WHERE title='부끄럽다'
;
UPDATE emotion
SET example='길 잃은 강아지가 불쌍해서 데려와 돌봤다.'
WHERE title='불쌍하다'
;
UPDATE emotion
SET example='연이은 불운으로 인해 불행한 날들을 보내고 있다.'
WHERE title='불행하다'
;
UPDATE emotion
SET example='전쟁으로 인해 삶이 비참해진 사람들의 이야기를 듣고 마음이 아팠다.'
WHERE title='비참하다'
;
UPDATE emotion
SET example='사랑하는 사람을 잃고 비탄에 빠져있다.'
WHERE title='비탄하다'
;
UPDATE emotion
SET example='친구의 갑작스러운 사고 소식에 비통한 마음을 감출 수 없었다.'
WHERE title='비통하다'
;
UPDATE emotion
SET example='어리석은 선택이 뼈저리게 후회스럽다.'
WHERE title='뼈저리다'
;
UPDATE emotion
SET example='그의 부재가 마음속 깊이 사무쳐서 눈물이 멈추지 않았다.'
WHERE title='사무치다'
;
UPDATE emotion
SET example='소중한 물건을 잃어버리고 나니 왠지 모를 상실감이 들었다.'
WHERE title='상실감 들다'
;
UPDATE emotion
SET example='억울한 일을 당하고 나니 눈물이 나도록 서러웠다.'
WHERE title='서럽다'
;
UPDATE emotion
SET example='기대했던 일이 이루어지지 않아서 서운한 마음이 들었다.'
WHERE title='서운하다'
;
UPDATE emotion
SET example='친구와의 이별이 더욱 섭섭하게 느껴졌다.'
WHERE title='섭섭하다'
;
UPDATE emotion
SET example='계획했던 일이 모두 엉망이 되어 속상했다.'
WHERE title='속상하다'
;
UPDATE emotion
SET example='혼자서만 걱정하며 속앓이하던 내 모습을 되돌아보았다.'
WHERE title='속앓이하다'
;
UPDATE emotion
SET example='잘못된 일을 하고 나서 어떻게 할지 몰라 송구한 마음뿐이었다.'
WHERE title='송구하다'
;
UPDATE emotion
SET example='고요한 산사에서의 시간은 마음을 숙연하게 만들었다.'
WHERE title='숙연하다'
;
UPDATE emotion
SET example='그녀는 헤어진 연인을 생각하며 슬퍼하였다.'
WHERE title='슬퍼하다'
;
UPDATE emotion
SET example='결과가 기대에 미치지 못해 실망하고 말았다.'
WHERE title='실망하다'
;
UPDATE emotion
SET example='그의 표정이 심각해서 무슨 일이 있는지 물어봤다.'
WHERE title='심각하다'
;
UPDATE emotion
SET example='마음이 심란해서 아무 일에도 집중할 수 없었다.'
WHERE title='심란하다'
;
UPDATE emotion
SET example='부모님은 나의 진로에 대해 심려하셨다.'
WHERE title='심려하다'
;
UPDATE emotion
SET example='이사 전날 밤, 마음이 싱숭생숭해서 잠이 오지 않았다.'
WHERE title='싱숭생숭하다'
;
UPDATE emotion
SET example='혼자 걷는 길이 쓸쓸하게 느껴졌다.'
WHERE title='쓸쓸하다'
;
UPDATE emotion
SET example='결과는 좋았지만 과정이 마음에 들지 않아 씁쓸했다.'
WHERE title='씁쓸하다'
;
UPDATE emotion
SET example='소중한 기회를 놓쳐서 아깝다는 생각이 들었다.'
WHERE title='아깝다'
;
UPDATE emotion
SET example='어린 시절의 추억이 아련하게 떠올랐다.'
WHERE title='아련하다'
;
UPDATE emotion
SET example='여행이 끝나고 집에 돌아오니 아쉬운 마음이 들었다.'
WHERE title='아쉽다'
;
UPDATE emotion
SET example='길에서 길 잃은 강아지를 보니 안쓰러운 마음이 들었다.'
WHERE title='안쓰럽다'
;
UPDATE emotion
SET example='친구의 실패 소식을 듣고 안타까운 마음을 감출 수 없었다.'
WHERE title='안타깝다'
;
UPDATE emotion
SET example='장래에 대한 생각을 하니 암담한 기분이 들었다.'
WHERE title='암담하다'
;
UPDATE emotion
SET example='계속되는 비로 인해 암울한 날들이 이어졌다.'
WHERE title='암울하다'
;
UPDATE emotion
SET example='사랑하는 사람이 떠나버려서 마음이 애끓었다.'
WHERE title='애끓다'
;
UPDATE emotion
SET example='영화의 슬픈 결말에 마음이 애달팠다.'
WHERE title='애달프다'
;
UPDATE emotion
SET example='고인의 장례식에서 모두가 애도하며 눈물을 흘렸다.'
WHERE title='애도하다'
;
UPDATE emotion
SET example='그가 떠났다는 소식을 듣고 애석한 마음이 들었다.'
WHERE title='애석하다'
;
UPDATE emotion
SET example='가냘픈 목소리로 노래를 부르는 모습이 애잔했다.'
WHERE title='애잔하다'
;
UPDATE emotion
SET example='길 위에서 추위에 떨고 있는 고양이가 애처로웠다.'
WHERE title='애처롭다'
;
UPDATE emotion
SET example='친구의 갑작스러운 사고 소식을 듣고 애통한 마음을 가눌 수 없었다.'
WHERE title='애통하다'
;
UPDATE emotion
SET example='사랑하는 사람과의 이별이 다가오니 애틋한 감정이 밀려왔다.'
WHERE title='애틋하다'
;
UPDATE emotion
SET example='오랜 친구가 연락을 끊어버려서 야속한 마음이 들었다.'
WHERE title='야속하다'
;
UPDATE emotion
SET example='아무 잘못도 없는데 억울하게 오해를 받았다.'
WHERE title='억울하다'
;
UPDATE emotion
SET example='시험 결과가 나올까 봐 염려하며 밤잠을 설쳤다.'
WHERE title='염려하다'
;
UPDATE emotion
SET example='혼자 집에 있을 때면 유난히 외로운 기분이 든다.'
WHERE title='외롭다'
;
UPDATE emotion
SET example='비 오는 날에는 왠지 모르게 우울한 기분이 든다.'
WHERE title='우울하다'
;
UPDATE emotion
SET example='슬픈 영화를 보고 눈물이 나서 울고 말았다.'
WHERE title='울다'
;
UPDATE emotion
SET example='선생님께 혼나고 나서 울먹이며 사과했다.'
WHERE title='울먹이다'
;
UPDATE emotion
SET example='상실의 고통에 울부짖으며 하늘을 향해 외쳤다.'
WHERE title='울부짖다'
;
UPDATE emotion
SET example='친구에게 부당한 대우를 받았을 때 울분이 치밀어 올랐다.'
WHERE title='울분하다'
;
UPDATE emotion
SET example='비가 오는 날에는 괜히 마음이 울적해진다.'
WHERE title='울적하다'
;
UPDATE emotion
SET example='그 영화의 마지막 장면에서 갑자기 눈물이 울컥 쏟아졌다.'
WHERE title='울컥하다'
;
UPDATE emotion
SET example='오해로 인해 나를 믿어주지 않는 친구에게 원통함을 느꼈다.'
WHERE title='원통하다'
;
UPDATE emotion
SET example='사람들 앞에서 발표를 하려니 위축되어 목소리가 작아졌다.'
WHERE title='위축되다'
;
UPDATE emotion
SET example='친구와의 약속을 지키지 못해 유감스럽다.'
WHERE title='유감스럽다'
;
UPDATE emotion
SET example='날씨가 흐리니 마음도 음울해졌다.'
WHERE title='음울하다'
;
UPDATE emotion
SET example='시험에서 실수한 나 자신을 자책했다.'
WHERE title='자책하다'
;
UPDATE emotion
SET example='모든 일이 잘 풀리지 않아서 순간 자포자기하고 싶었다.'
WHERE title='자포자기하다'
;
UPDATE emotion
SET example='혼자 있는 시간이 많아지니 적적함이 느껴졌다.'
WHERE title='적적하다'
;
UPDATE emotion
SET example='중요한 발표를 앞두고 전전긍긍하며 잠을 설쳤다.'
WHERE title='전전긍긍하다'
;
UPDATE emotion
SET example='사랑하는 이를 잃고 절규하며 슬픔에 잠겼다.'
WHERE title='절규하다'
;
UPDATE emotion
SET example='꿈꿔왔던 기회를 놓치고 절망했다.'
WHERE title='절망하다'
;
UPDATE emotion
SET example='과제 마감일이 다가오자 절박한 마음이 들었다.'
WHERE title='절박하다'
;
UPDATE emotion
SET example='가족의 소중함을 절실히 깨달았다.'
WHERE title='절실하다'
;
UPDATE emotion
SET example='헤어진 연인에게 다시 돌아와 달라고 절절매었다.'
WHERE title='절절매다'
;
UPDATE emotion
SET example='그의 진심 어린 편지가 절절하게 마음에 와 닿았다.'
WHERE title='절절하다'
;
UPDATE emotion
SET example='계획했던 일이 좌절되어 한동안 낙심했다.'
WHERE title='좌절되다'
;
UPDATE emotion
SET example='실수로 친구의 물건을 망가뜨려서 몹시 죄송했다.'
WHERE title='죄송하다'
;
UPDATE emotion
SET example='거짓말을 하고 나니 죄책감이 들었다.'
WHERE title='죄책감 들다'
;
UPDATE emotion
SET example='큰 소리로 발표하라는 선생님의 말씀에 주눅들어 목소리가 작아졌다.'
WHERE title='주눅들다'
;
UPDATE emotion
SET example='길가에서 홀로 앉아 우는 아이를 보니 마음이 짠했다.'
WHERE title='짠하다'
;
UPDATE emotion
SET example='갑작스러운 질문에 준비가 안 되어 쩔쩔맸다.'
WHERE title='쩔쩔매다'
;
UPDATE emotion
SET example='오랜만에 만난 친구의 따뜻한 인사말에 가슴이 찡했다.'
WHERE title='찡하다'
;
UPDATE emotion
SET example='친구와의 오해를 풀고 나니 마음이 착잡했다.'
WHERE title='착잡하다'
;
UPDATE emotion
SET example='이번 시험 결과를 보고 참담한 기분이 들었다.'
WHERE title='참담하다'
;
UPDATE emotion
SET example='전쟁의 참혹한 장면을 뉴스에서 보며 눈물을 흘렸다.'
WHERE title='참혹하다'
;
UPDATE emotion
SET example='과거의 잘못을 반성하며 깊이 참회했다.'
WHERE title='참회하다'
;
UPDATE emotion
SET example='사람들 앞에서 넘어져서 너무 창피했다.'
WHERE title='창피하다'
;
UPDATE emotion
SET example='비 오는 날 혼자 집으로 돌아가는 길이 처량하게 느껴졌다.'
WHERE title='처량하다'
;
UPDATE emotion
SET example='이별의 순간이 이렇게 처절할 줄은 몰랐다.'
WHERE title='처절하다'
;
UPDATE emotion
SET example='그의 처참한 눈빛이 아직도 잊혀지지 않는다.'
WHERE title='처참하다'
;
UPDATE emotion
SET example='그의 청승맞은 모습에 마음이 편치 않았다.'
WHERE title='청승맞다'
;
UPDATE emotion
SET example='거울 속의 초라한 내 모습을 보며 한숨이 나왔다.'
WHERE title='초라하다'
;
UPDATE emotion
SET example='길거리에서 구걸하는 노인을 보며 측은한 마음이 들었다.'
WHERE title='측은하다'
;
UPDATE emotion
SET example='계속되는 실패에 마음이 점점 침울해졌다.'
WHERE title='침울하다'
;
UPDATE emotion
SET example='그의 침통한 표정을 보니 무슨 일이 있는 것 같았다.'
WHERE title='침통하다'
;
UPDATE emotion
SET example='그의 재능에 탄복하며 더욱 열심히 노력하기로 했다.'
WHERE title='탄복하다'
;
UPDATE emotion
SET example='길고 긴 하루가 끝나고 나서 깊은 탄식을 내뱉었다.'
WHERE title='탄식하다'
;
UPDATE emotion
SET example='사랑하는 이를 잃고 통탄하며 하루를 보냈다.'
WHERE title='통탄하다'
;
UPDATE emotion
SET example='시험 결과를 보고 나도 모르게 한숨을 지었다.'
WHERE title='한숨짓다'
;
UPDATE emotion
SET example='그때의 잘못된 선택이 한스럽게 느껴졌다.'
WHERE title='한스럽다'
;
UPDATE emotion
SET example='그는 자신의 실수를 한탄하며 고개를 떨구었다.'
WHERE title='한탄하다'
;
UPDATE emotion
SET example='오랫동안 준비한 일이 실패로 끝나서 허무했다.'
WHERE title='허무하다'
;
UPDATE emotion
SET example='친구가 떠난 후 집이 너무 허전하게 느껴졌다.'
WHERE title='허전하다'
;
UPDATE emotion
SET example='기대했던 일이 실패로 돌아가자 허탈한 기분이 들었다.'
WHERE title='허탈하다'
;
UPDATE emotion
SET example='나는 지난 결정에 대해 깊이 후회하고 있다.'
WHERE title='후회하다'
;
UPDATE emotion
SET example='그의 방은 아무도 살지 않는 것처럼 휑했다.'
WHERE title='휑하다'
;
UPDATE emotion
SET example='실수를 통해 자신의 부족함을 각성하게 되었다.'
WHERE title='각성되다'
;
UPDATE emotion
SET example='그는 두 가지 선택지 사이에서 갈등하고 있었다.'
WHERE title='갈등하다'
;
UPDATE emotion
SET example='그는 결과를 듣고도 덤덤한 표정을 지었다.'
WHERE title='덤덤하다'
;
UPDATE emotion
SET example='나는 중요한 문서를 다룰 때 항상 조심스럽다.'
WHERE title='조심스럽다'
;
UPDATE emotion
SET example='그녀는 어려운 상황에서도 초연하게 행동했다.'
WHERE title='초연하다'
;
UPDATE emotion
SET example='지하철 안은 너무 갑갑해서 숨이 막힐 것 같았다.'
WHERE title='갑갑하다'
;
UPDATE emotion
SET example='그의 연설은 고리타분해서 집중하기 어려웠다.'
WHERE title='고리타분하다'
;
UPDATE emotion
SET example='오늘은 아무것도 하기 싫고 모든 게 귀찮다.'
WHERE title='귀찮다'
;
UPDATE emotion
SET example='방 안이 너무 답답해서 창문을 열었다.'
WHERE title='답답하다'
;
UPDATE emotion
SET example='긴 회의는 따분해서 집중하기 힘들었다.'
WHERE title='따분하다'
;
UPDATE emotion
SET example='그의 제안이 떨떠름하게 느껴졌다.'
WHERE title='떨떠름하다'
;
UPDATE emotion
SET example='그의 설명은 왠지 마땅찮게 들렸다.'
WHERE title='마땅찮다'
;
UPDATE emotion
SET example='시험 결과가 기대에 미치지 못해 맥빠졌다.'
WHERE title='맥빠지다'
;
UPDATE emotion
SET example='주말 내내 집에만 있으니 무료해졌다.'
WHERE title='무료하다'
;
UPDATE emotion
SET example='연극장 의자가 너무 불편해서 공연을 온전히 즐기지 못했다.'
WHERE title='불편하다'
;
UPDATE emotion
SET example='오랜만에 만난 친구와 서먹하게 대화를 이어갔다.'
WHERE title='서먹하다'
;
UPDATE emotion
SET example='시답잖은 농담 때문에 분위기가 조금 어색해졌다.'
WHERE title='시답잖다'
;
UPDATE emotion
SET example='요즘 날씨가 신통찮아서 기분도 덩달아 가라앉는다.'
WHERE title='신통찮다'
;
UPDATE emotion
SET example='매일 같은 음식을 먹다 보니 싫증이 났다.'
WHERE title='싫증나다'
;
UPDATE emotion
SET example='그 영화에 대한 리뷰를 듣고 나니 심드렁해졌다.'
WHERE title='심드렁하다'
;
UPDATE emotion
SET example='비 오는 날 집에만 있으니 너무 심심하다.'
WHERE title='심심하다'
;
UPDATE emotion
SET example='처음 만난 사람과의 대화가 어색하게 느껴졌다.'
WHERE title='어색하다'
;
UPDATE emotion
SET example='기대했던 영화가 생각보다 재미없어서 실망했다.'
WHERE title='재미없다'
;
UPDATE emotion
SET example='반복되는 일상에 점점 지겨움을 느끼기 시작했다.'
WHERE title='지겹다'
;
UPDATE emotion
SET example='매일 반복되는 야근이 지긋지긋하다.'
WHERE title='지긋지긋하다'
;
UPDATE emotion
SET example='기나긴 회의가 지루하게 느껴졌다.'
WHERE title='지루하다'
;
UPDATE emotion
SET example='운동 후 물 한 잔이 간절히 갈증 나게 했다.'
WHERE title='갈증 나다'
;
UPDATE emotion
SET example='하루 종일 일하고 나니 몸이 고단하다.'
WHERE title='고단하다'
;
UPDATE emotion
SET example='이별 후의 시간이 너무나 고통스러웠다.'
WHERE title='고통스럽다'
;
UPDATE emotion
SET example='복잡한 문제를 해결하느라 골치가 아프다.'
WHERE title='골치아프다'
;
UPDATE emotion
SET example='마라톤을 완주한 후 기진맥진했다.'
WHERE title='기진맥진하다'
;
UPDATE emotion
SET example='큰 실수를 저지르고 나니 뼈아픈 후회가 밀려왔다.'
WHERE title='뼈아프다'
;
UPDATE emotion
SET example='어제 길에서 넘어져서 무릎이 아파서 제대로 걷지 못했다.'
WHERE title='아프다'
;
UPDATE emotion
SET example='시험 스트레스로 인해 머리가 지끈거린다.'
WHERE title='지끈거리다'
;
UPDATE emotion
SET example='친구가 파티에서 춤추는 모습을 보니 정말 가관이었다.'
WHERE title='가관이다'
;
UPDATE emotion
SET example='그의 거짓말은 너무나 가소롭고 뻔했다.'
WHERE title='가소롭다'
;
UPDATE emotion
SET example='그가 한 말은 정말 같잖아서 무시해 버렸다.'
WHERE title='같잖다'
;
UPDATE emotion
SET example='모르는 사람과 엘리베이터에 함께 있자니 거북한 느낌이 들었다.'
WHERE title='거북하다'
;
UPDATE emotion
SET example='그 사람의 목소리가 이상하게 거슬려서 집중이 되지 않았다.'
WHERE title='거슬리다'
;
UPDATE emotion
SET example='그의 비열한 행동을 보며 경멸할 수밖에 없었다.'
WHERE title='경멸하다'
;
UPDATE emotion
SET example='그는 중요한 회의 중에도 경박하게 행동해 모두를 불편하게 만들었다.'
WHERE title='경박하다'
;
UPDATE emotion
SET example='그 음식에서는 고약한 냄새가 나서 먹을 수가 없었다.'
WHERE title='고약하다'
;
UPDATE emotion
SET example='그의 복장은 정말 괴상해서 눈길을 끌었다.'
WHERE title='괴상하다'
;
UPDATE emotion
SET example='그 상사는 괴팍한 성격 때문에 직원들이 다가가기 어려워한다.'
WHERE title='괴팍하다'
;
UPDATE emotion
SET example='쓰레기 더미 옆을 지나가니 구역질날 정도로 냄새가 심했다.'
WHERE title='구역질나다'
;
UPDATE emotion
SET example='비가 온 뒤 구질구질한 길을 걸어야 해서 기분이 좋지 않다.'
WHERE title='구질구질하다'
;
UPDATE emotion
SET example='변명이 너무 구차해서 차라리 듣지 말 걸 그랬다.'
WHERE title='구차하다'
;
UPDATE emotion
SET example='그 제안은 뭔가 꺼림칙해서 쉽게 수락할 수 없었다.'
WHERE title='꺼림칙하다'
;
UPDATE emotion
SET example='그는 항상 꼴불견인 옷차림으로 나타나 주위를 당황하게 한다.'
WHERE title='꼴불견이다'
;
UPDATE emotion
SET example='그의 실수로 인해 남부끄러워 얼굴을 들 수가 없었다.'
WHERE title='남부끄럽다'
;
UPDATE emotion
SET example='매일 반복되는 일상이 이제는 정말 넌더리가 난다.'
WHERE title='넌더리 나다'
;
UPDATE emotion
SET example='그의 과장된 칭찬에 느글거려서 더 이상 듣고 싶지 않았다.'
WHERE title='느글거리다'
;
UPDATE emotion
SET example='기름진 음식을 먹고 나니 속이 너무 느끼했다.'
WHERE title='느끼하다'
;
UPDATE emotion
SET example='친구가 갑자기 돈을 빌려달라고 해서 달갑잖았다.'
WHERE title='달갑잖다'
;
UPDATE emotion
SET example='방 한구석에 먼지가 쌓여 있어서 정말 더럽게 느껴졌다.'
WHERE title='더럽다'
;
UPDATE emotion
SET example='길에서 이상한 옷을 입은 사람을 보고 망측하다고 생각했다.'
WHERE title='망측하다'
;
UPDATE emotion
SET example='그 친구는 항상 약속을 어겨서 못미덥다.'
WHERE title='못미덥다'
;
UPDATE emotion
SET example='상사가 내게 중요한 프로젝트를 맡기겠다고 해서 부담스러웠다.'
WHERE title='부담스럽다'
;
UPDATE emotion
SET example='그의 무례한 말투 때문에 불쾌한 기분이 들었다.'
WHERE title='불쾌하다'
;
UPDATE emotion
SET example='매일 같은 점심을 먹다 보니 이제는 신물 나기 시작했다.'
WHERE title='신물 나다'
;
UPDATE emotion
SET example='비 오는 날에 외출하는 것이 정말 싫다.'
WHERE title='싫다'
;
UPDATE emotion
SET example='썩은 냄새가 진동하는 쓰레기통을 열었을 때 정말 역겨웠다.'
WHERE title='역겹다'
;
UPDATE emotion
SET example='친구가 어설프게 농담을 해서 우스웠다.'
WHERE title='우습다'
;
UPDATE emotion
SET example='그 사람의 이기적인 행동을 보고 정떨어졌다.'
WHERE title='정떨어지다'
;
UPDATE emotion
SET example='그 사람의 냉정한 말투가 정말 지독하게 느껴졌다.'
WHERE title='지독하다'
;
UPDATE emotion
SET example='같은 이야기를 반복해서 듣다 보니 진저리가 났다.'
WHERE title='진저리나다'
;
UPDATE emotion
SET example='벽에 기어 다니는 벌레를 보고 정말 징그러웠다.'
WHERE title='징그럽다'
;
UPDATE emotion
SET example='친구가 갑자기 약속을 취소해서 무슨 일이 있는지 찜찜하다.'
WHERE title='찜찜하다'
;
UPDATE emotion
SET example='그의 허세 가득한 이야기에 코웃음을 치고 말았다.'
WHERE title='코웃음 치다'
;
UPDATE emotion
SET example='중요한 일을 깜빡 잊어버린 내 자신이 한심하게 느껴졌다.'
WHERE title='한심하다'
;
UPDATE emotion
SET example='이상한 소문이 돌고 있어서 해괴하다고 생각했다.'
WHERE title='해괴하다'
;
UPDATE emotion
SET example='그 사람의 무례한 행동이 너무 흉측해서 눈을 돌렸다.'
WHERE title='흉측하다'
;
UPDATE emotion
SET example='매일 아침마다 커피를 갈구하며 카페에 들른다.'
WHERE title='갈구하다'
;
UPDATE emotion
SET example='나는 항상 자유로운 여행을 갈망한다.'
WHERE title='갈망하다'
;
UPDATE emotion
SET example='맛을 보니 너무 감질나서 더 먹고 싶어졌다.'
WHERE title='감질나다'
;
UPDATE emotion
SET example='그 영화의 결말이 너무 궁금해서 잠을 이룰 수 없었다.'
WHERE title='궁금하다'
;
UPDATE emotion
SET example='친구가 말한 이야기를 반신반의하며 듣고 있었다.'
WHERE title='반신반의하다'
;
UPDATE emotion
SET example='친구가 새 차를 샀다는 소식을 듣고 부러워했다.'
WHERE title='부러워하다'
;
UPDATE emotion
SET example='처음 본 마술쇼가 너무 신기해서 눈을 뗄 수 없었다.'
WHERE title='신기하다'
;
UPDATE emotion
SET example='깊은 산속의 호수는 언제나 신비롭게 느껴진다.'
WHERE title='신비롭다'
;
UPDATE emotion
SET example='그 사람의 행동은 정말 아리송해서 이해하기 어려웠다.'
WHERE title='아리송하다'
;
UPDATE emotion
SET example='이 수학 문제는 알쏭달쏭해서 풀기가 힘들었다.'
WHERE title='알쏭달쏭하다'
;
UPDATE emotion
SET example='롤러코스터를 탈 때마다 짜릿한 기분이 든다.'
WHERE title='짜릿하다'
;
UPDATE emotion
SET example='친구의 예쁜 가방이 탐나서 같은 디자인을 사고 싶었다.'
WHERE title='탐나다'
;
UPDATE emotion
SET example='휴가를 학수고대하며 달력을 보며 날짜를 세고 있다.'
WHERE title='학수고대하다'
;
UPDATE emotion
SET example='그 책의 첫 장부터 흥미로워서 손을 놓을 수가 없었다.'
WHERE title='흥미롭다'

;