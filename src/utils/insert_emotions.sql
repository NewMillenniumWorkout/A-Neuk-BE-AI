-- 테이블 생성
CREATE TABLE IF NOT EXISTS emotion (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    example TEXT
);

INSERT INTO emotion (title, example)
VALUES
    ('겁나다', NULL),
    ('공포스럽다', NULL),
    ('급박하다', NULL),
    ('긴박하다', NULL),
    ('긴장되다', NULL),
    ('끔찍하다', NULL),
    ('낯설다', NULL),
    ('노심초사하다', NULL),
    ('두렵다', NULL),
    ('몸서리치다', NULL),
    ('무섭다', NULL),
    ('무시무시하다', NULL),
    ('불안정하다', NULL),
    ('불안하다', NULL),
    ('살벌하다', NULL),
    ('새파래지다', NULL),
    ('섬뜩하다', NULL),
    ('소름끼치다', NULL),
    ('스산하다', NULL),
    ('아슬아슬하다', NULL),
    ('아찔하다', NULL),
    ('안절부절하다', NULL),
    ('오싹하다', NULL),
    ('으스스하다', NULL),
    ('을씨년스럽다', NULL),
    ('잔인하다', NULL),
    ('잔혹하다', NULL),
    ('조마조마하다', NULL),
    ('조바심하다', NULL),
    ('질겁하다', NULL),
    ('초조하다', NULL),
    ('가볍다', NULL),
    ('가뿐하다', NULL),
    ('감개무량하다', NULL),
    ('감격하다', NULL),
    ('감동하다', NULL),
    ('감명깊다', NULL),
    ('감미롭다', NULL),
    ('감복하다', NULL),
    ('감사하다', NULL),
    ('감회가 새롭다', NULL),
    ('감흥을 불러일으키다', NULL),
    ('경쾌하다', NULL),
    ('고맙다', NULL),
    ('고취되다', NULL),
    ('근사하다', NULL),
    ('기분 좋다', NULL),
    ('기쁘다', NULL),
    ('낭만적이다', NULL),
    ('달갑다', NULL),
    ('대견하다', NULL),
    ('두근거리다', NULL),
    ('따뜻하다', NULL),
    ('따스하다', NULL),
    ('만족하다', NULL),
    ('매력적이다', NULL),
    ('반갑다', NULL),
    ('보기 좋다', NULL),
    ('뿌듯하다', NULL),
    ('사랑스럽다', NULL),
    ('상기되다', NULL),
    ('상쾌하다', NULL),
    ('상큼하다', NULL),
    ('설레다', NULL),
    ('속 시원하다', NULL),
    ('신나다', NULL),
    ('신명나다', NULL),
    ('신바람 나다', NULL),
    ('신선하다', NULL),
    ('싱글벙글하다', NULL),
    ('쑥스럽다', NULL),
    ('씰룩거리다', NULL),
    ('어여쁘다', NULL),
    ('예쁘다', NULL),
    ('우아하다', NULL),
    ('웃다', NULL),
    ('웃어넘기다', NULL),
    ('유쾌하다', NULL),
    ('으쓱하다', NULL),
    ('자부하다', NULL),
    ('재미있다', NULL),
    ('좋다', NULL),
    ('즐겁다', NULL),
    ('천만다행이다', NULL),
    ('친근하다', NULL),
    ('친숙하다', NULL),
    ('콩닥거리다', NULL),
    ('쾌적하다', NULL),
    ('통쾌하다', NULL),
    ('편안하다', NULL),
    ('행복하다', NULL),
    ('후련하다', NULL),
    ('훌륭하다', NULL),
    ('흐뭇하다', NULL),
    ('흡족하다', NULL),
    ('흥겹다', NULL),
    ('희희낙락하다', NULL),
    ('히죽거리다', NULL),
    ('개운찮다', NULL),
    ('겸연쩍다', NULL),
    ('계면쩍다', NULL),
    ('곤란하다', NULL),
    ('기고만장하다', NULL),
    ('낯간지럽다', NULL),
    ('낯뜨겁다', NULL),
    ('노파심이 들다', NULL),
    ('머쓱하다', NULL),
    ('멋쩍다', NULL),
    ('무안하다', NULL),
    ('민망하다', NULL),
    ('오그라들다', NULL),
    ('쭈뼛거리다', NULL),
    ('감탄하다', NULL),
    ('갑작스럽다', NULL),
    ('경악하다', NULL),
    ('경이롭다', NULL),
    ('곤혹스럽다', NULL),
    ('급작스럽다', NULL),
    ('기겁하다', NULL),
    ('기막히다', NULL),
    ('기묘하다', NULL),
    ('기상천외', NULL),
    ('기이하다', NULL),
    ('기절초풍하다', NULL),
    ('기절하다', NULL),
    ('까무러치다', NULL),
    ('난감하다', NULL),
    ('놀랍다', NULL),
    ('당혹하다', NULL),
    ('당황하다', NULL),
    ('뜨금하다', NULL),
    ('뜨악하다', NULL),
    ('만만찮다', NULL),
    ('쇼킹하다', NULL),
    ('아연실색하다', NULL),
    ('어리둥절하다', NULL),
    ('얼떨떨하다', NULL),
    ('움찔하다', NULL),
    ('이상하다', NULL),
    ('전율하다', NULL),
    ('철렁하다', NULL),
    ('충격적이다', NULL),
    ('휘둥그레지다', NULL),
    ('흠칫하다', NULL),
    ('가당찮다', NULL),
    ('가증스럽다', NULL),
    ('거지같다', NULL),
    ('격노하다', NULL),
    ('격분하다', NULL),
    ('격앙되다', NULL),
    ('격양되다', NULL),
    ('격해지다', NULL),
    ('괘씸하다', NULL),
    ('굴욕감 들다', NULL),
    ('기분 나쁘다', NULL),
    ('노여워하다', NULL),
    ('모멸감 들다', NULL),
    ('모욕적이다', NULL),
    ('못되다', NULL),
    ('못마땅하다', NULL),
    ('무시당하다', NULL),
    ('밉다', NULL),
    ('발칙하다', NULL),
    ('복수심 들다', NULL),
    ('분개하다', NULL),
    ('분노하다', NULL),
    ('분통터지다', NULL),
    ('분하다', NULL),
    ('불만스럽다', NULL),
    ('불만족하다', NULL),
    ('불유쾌하다', NULL),
    ('비딱하다', NULL),
    ('비아냥거리다', NULL),
    ('빈정거리다', NULL),
    ('뾰루퉁하다', NULL),
    ('삐치다', NULL),
    ('속썩이다', NULL),
    ('수치스럽다', NULL),
    ('신경질나다', NULL),
    ('심술궂다', NULL),
    ('심통나다', NULL),
    ('씩씩거리다', NULL),
    ('아니꼽다', NULL),
    ('야박하다', NULL),
    ('야비하다', NULL),
    ('약오르다', NULL),
    ('얄밉다', NULL),
    ('어이없다', NULL),
    ('언짢다', NULL),
    ('울화통 터지다', NULL),
    ('원망하다', NULL),
    ('의심스럽다', NULL),
    ('증오하다', NULL),
    ('진노하다', NULL),
    ('질투하다', NULL),
    ('짜증나다', NULL),
    ('치가 떨리다', NULL),
    ('치밀어오르다', NULL),
    ('치욕적이다', NULL),
    ('흥분하다', NULL),
    ('가련하다', NULL),
    ('가슴 아프다', NULL),
    ('가엾다', NULL),
    ('가혹하다', NULL),
    ('각박하다', NULL),
    ('간절하다', NULL),
    ('걱정하다', NULL),
    ('고달프다', NULL),
    ('고독하다', NULL),
    ('곤욕스럽다', NULL),
    ('공허하다', NULL),
    ('괴롭다', NULL),
    ('구슬프다', NULL),
    ('그리워하다', NULL),
    ('근심스럽다', NULL),
    ('글썽글썽하다', NULL),
    ('기구하다', NULL),
    ('기운 없다', NULL),
    ('낙담하다', NULL),
    ('낙망하다', NULL),
    ('낙심하다', NULL),
    ('난처하다', NULL),
    ('남부럽다', NULL),
    ('낭패스럽다', NULL),
    ('냉혹하다', NULL),
    ('눈물겹다', NULL),
    ('뒤숭숭하다', NULL),
    ('망막하다', NULL),
    ('망연자실하다', NULL),
    ('먹먹하다', NULL),
    ('뭉클하다', NULL),
    ('미안하다', NULL),
    ('복받치다', NULL),
    ('부끄럽다', NULL),
    ('불쌍하다', NULL),
    ('불행하다', NULL),
    ('비참하다', NULL),
    ('비탄하다', NULL),
    ('비통하다', NULL),
    ('뼈저리다', NULL),
    ('사무치다', NULL),
    ('상실감 들다', NULL),
    ('서럽다', NULL),
    ('서운하다', NULL),
    ('섭섭하다', NULL),
    ('속상하다', NULL),
    ('속앓이하다', NULL),
    ('송구하다', NULL),
    ('숙연하다', NULL),
    ('슬퍼하다', NULL),
    ('실망하다', NULL),
    ('심각하다', NULL),
    ('심란하다', NULL),
    ('심려하다', NULL),
    ('싱숭생숭하다', NULL),
    ('쓸쓸하다', NULL),
    ('씁쓸하다', NULL),
    ('아깝다', NULL),
    ('아련하다', NULL),
    ('아쉽다', NULL),
    ('안쓰럽다', NULL),
    ('안타깝다', NULL),
    ('암담하다', NULL),
    ('암울하다', NULL),
    ('애끓다', NULL),
    ('애달프다', NULL),
    ('애도하다', NULL),
    ('애석하다', NULL),
    ('애잔하다', NULL),
    ('애처롭다', NULL),
    ('애통하다', NULL),
    ('애틋하다', NULL),
    ('야속하다', NULL),
    ('억울하다', NULL),
    ('염려하다', NULL),
    ('외롭다', NULL),
    ('우울하다', NULL),
    ('울다', NULL),
    ('울먹이다', NULL),
    ('울부짖다', NULL),
    ('울분하다', NULL),
    ('울적하다', NULL),
    ('울컥하다', NULL),
    ('원통하다', NULL),
    ('위축되다', NULL),
    ('유감스럽다', NULL),
    ('음울하다', NULL),
    ('자책하다', NULL),
    ('자포자기하다', NULL),
    ('적적하다', NULL),
    ('전전긍긍하다', NULL),
    ('절규하다', NULL),
    ('절망하다', NULL),
    ('절박하다', NULL),
    ('절실하다', NULL),
    ('절절매다', NULL),
    ('절절하다', NULL),
    ('좌절되다', NULL),
    ('죄송하다', NULL),
    ('죄책감 들다', NULL),
    ('주눅들다', NULL),
    ('짠하다', NULL),
    ('쩔쩔매다', NULL),
    ('찡하다', NULL),
    ('착잡하다', NULL),
    ('참담하다', NULL),
    ('참혹하다', NULL),
    ('참회하다', NULL),
    ('창피하다', NULL),
    ('처량하다', NULL),
    ('처절하다', NULL),
    ('처참하다', NULL),
    ('청승맞다', NULL),
    ('초라하다', NULL),
    ('측은하다', NULL),
    ('침울하다', NULL),
    ('침통하다', NULL),
    ('탄복하다', NULL),
    ('탄식하다', NULL),
    ('통탄하다', NULL),
    ('한숨짓다', NULL),
    ('한스럽다', NULL),
    ('한탄하다', NULL),
    ('허무하다', NULL),
    ('허전하다', NULL),
    ('허탈하다', NULL),
    ('후회하다', NULL),
    ('휑하다', NULL),
    ('각성되다', NULL),
    ('갈등하다', NULL),
    ('덤덤하다', NULL),
    ('조심스럽다', NULL),
    ('초연하다', NULL),
    ('갑갑하다', NULL),
    ('고리타분하다', NULL),
    ('귀찮다', NULL),
    ('답답하다', NULL),
    ('따분하다', NULL),
    ('떨떠름하다', NULL),
    ('마땅찮다', NULL),
    ('맥빠지다', NULL),
    ('무료하다', NULL),
    ('불편하다', NULL),
    ('서먹하다', NULL),
    ('시답잖다', NULL),
    ('신통찮다', NULL),
    ('싫증나다', NULL),
    ('심드렁하다', NULL),
    ('심심하다', NULL),
    ('어색하다', NULL),
    ('재미없다', NULL),
    ('지겹다', NULL),
    ('지긋지긋하다', NULL),
    ('지루하다', NULL),
    ('갈증 나다', NULL),
    ('고단하다', NULL),
    ('고통스럽다', NULL),
    ('골치아프다', NULL),
    ('기진맥진하다', NULL),
    ('뼈아프다', NULL),
    ('아프다', NULL),
    ('지끈거리다', NULL),
    ('가관이다', NULL),
    ('가소롭다', NULL),
    ('같잖다', NULL),
    ('거북하다', NULL),
    ('거슬리다', NULL),
    ('경멸하다', NULL),
    ('경박하다', NULL),
    ('고약하다', NULL),
    ('괴상하다', NULL),
    ('괴팍하다', NULL),
    ('구역질나다', NULL),
    ('구질구질하다', NULL),
    ('구차하다', NULL),
    ('꺼림칙하다', NULL),
    ('꼴불견이다', NULL),
    ('남부끄럽다', NULL),
    ('넌더리 나다', NULL),
    ('느글거리다', NULL),
    ('느끼하다', NULL),
    ('달갑잖다', NULL),
    ('더럽다', NULL),
    ('망측하다', NULL),
    ('못미덥다', NULL),
    ('부담스럽다', NULL),
    ('불쾌하다', NULL),
    ('신물 나다', NULL),
    ('싫다', NULL),
    ('역겹다', NULL),
    ('우습다', NULL),
    ('정떨어지다', NULL),
    ('지독하다', NULL),
    ('진저리나다', NULL),
    ('징그럽다', NULL),
    ('찜찜하다', NULL),
    ('코웃음 치다', NULL),
    ('한심하다', NULL),
    ('해괴하다', NULL),
    ('흉측하다', NULL),
    ('갈구하다', NULL),
    ('갈망하다', NULL),
    ('감질나다', NULL),
    ('궁금하다', NULL),
    ('반신반의하다', NULL),
    ('부러워하다', NULL),
    ('신기하다', NULL),
    ('신비롭다', NULL),
    ('아리송하다', NULL),
    ('알쏭달쏭하다', NULL),
    ('짜릿하다', NULL),
    ('탐나다', NULL),
    ('학수고대하다', NULL),
    ('흥미롭다', NULL)
;