from pymongo import MongoClient

# Kết nối MongoDB
client = MongoClient('mongodb://localhost:27017/')
jsondb = client['math_quiz']
collection = jsondb['questions']

# Dữ liệu câu hỏi
questions_data = {
    "topic": "Đề số 1", 
    "questions": [
        {
            "question": "Cho đồ thị hàm số $y = ax^{4} + bx^{2} + c$ có đồ thị là đường cong trong hình bên. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?",
            "options": ["A. $(-\infty;-1)$", "B. $(-\infty;1)$", "C. $(-1;1)$", "D. $(1;+\infty )$"],
            "answer": 3,
            "explanation": "Dựa vào đồ thị ta có: hàm số đã cho nghịch biến trên khoảng $(1;+\infty )$"
        },
        {
            "question": "Tập xác định của hàm số $y=(5-x)^{\frac{2}{3}}$ là",
            "options": ["A. $(-\infty ;5)$", "B. $(5;+\infty )$", "C. $\Re$", "D. $\Re\setminus \left\{ 5\right\}$"],
            "answer": 0,
            "explanation": "Ta có $\frac{2}{3}\notin\mathbb{Z}$ nên hàm số $(5-x)^{\frac{2}{3}}$ xác định khi $5-x> 0\Rightarrow x< 5$."
        },
        {
            "question": "Trong không gian $Oxyz$, cho mặt cầu $\left ( S \right )$:$(x-3)^{2}+(y+2)^2+(z-1)^2=16$. Tọa độ tâm $I$ và bán kính $R$ của $\left ( S \right )$ là",
            "options": ["A. $I(3;-2;1), R=4$", "B. $I(-3;2;-1), R=4$", "C. $I(-3;2;-1), R=16$", "D. $I(3;-2;1), R=16$"],
            "answer": 0,
            "explanation": "Ta có $\left ( S \right )$:$(x-3)^{2}+(y+2)^2+(z-1)^2=16$. Có tâm $I(3;-2;1), R=4$."
        },
        {
            "question": "Nếu $\int_{2}^{5}f\left ( x \right )dx=-2$ và $\int_{2}^{5}g\left ( x \right )dx=3$ thì $\int_{2}^{5}\left [ 3f\left ( x \right )+ 5g\left ( x \right ) \right ]dx$ bằng",
            "options": ["A. 21", "B. 12", "C. 15", "D. 9"],
            "answer": 3,
            "explanation": "Ta có $3\int_{2}^{5}\left f\left ( x \right )dx + 5\int_{2}^{5}g\left ( x \right ) \right ]dx = 3.(-2) + 5.3 = 9$."
        },
        {
            "question": "Tập nghiệm của phương trình $log_{2}\left ( 2x^{2}-3 \right )=log_{2}\left ( 2-3x \right )$ là",
            "options": ["A. $\left\{\frac{5}{2};-1 \right\}$", "B. $\left\{\frac{5}{2} \right\}$", "C. $\left\{-1 \right\}$", "D. $\left\{-\frac{5}{2};-1 \right\}$"],
            "answer": 1,
            "explanation": "Điều kiện $\left\{\begin{matrix}2x^{2}-3 > 0 \\2-3x > 0\end{matrix}\right.$ \nVới điều kiện trên phương trình trở thành: $2x^2-3=2-3x\Leftrightarrow 2x^2+3x-5=0\Leftrightarrow x=1 \vee x=\frac{-5}{2}$ \nSo với điều kiện, nghiệm phương trình là: $x=\frac{-5}{2}$. \nVậy tập nghiệm của phương trình $log_{2}\left ( 2x^{2}-3 \right )=log_{2}\left ( 2-3x \right )$ là $S=\left\{\frac{5}{2} \right\}$."
        },
        {
            "question": "Tiệm cận ngang của đồ thị hàm số $y=\frac{4-3x}{x-2}$ là đường thẳng có phương trình",
            "options": ["A. $y=4$", "B. $y=-3$", "C. $x=2$", "D. $y=\frac{3}{2}$"],
            "answer": 1,
            "explanation": "Tập xác định $D=\mathbb{R}\setminus \left\{2 \right\}$. \nTa có $\displaystyle \lim_{X \to +\infty } y =\displaystyle \lim_{x \to +\infty}\frac{4-3x}{x-2}=\frac{-3}{1}=3$. \nVậy tiệm cận ngang của đồ thị hàm số $y=\frac{4-3x}{x-2}$ là đường thẳng có phương trình $y=-3$"
        },
        {
            "question": "Cho hàm số $y=f\left ( x \right )$ có đạo hàm $f'\left ( x \right )=\left ( x-1 \right )^2\left ( x^2-3x+2 \right ), \forall x\in \mathbb{R}$. Số điểm cực trị của hàm số đã cho là",
            "options": ["A. $4$", "B. $2$", "C. $3$", "D. $1$"],
            "answer": 1,
            "explanation": "Ta có $f'\left ( x \right )=0\Leftrightarrow \left ( x-1 \right )^2\left ( x^2-3x+2 \right )\Leftrightarrow x=1 \vee x=2$ \nLập bảng xét dấu:(học sinh tự vẽ) \nTa thấy $f'\left ( x \right )$ đổi dấu 2 lần khi qua $x=1, x=2$ nên hàm số có 2 điểm cực trị."
        },
        {
            "question": "Cho khối chóp có diện tích đáy bằng $6a^2$ và chiều cao bằng $4a$.Thể tích khối chóp đã cho bằng",
            "options": ["A. $8a^2$", "B. $12a^3$", "C. $8a^3$", "D. $24a^3$"],
            "answer": 2,
            "explanation": "Ta có thể tích khối chóp đã cho là: $V=\frac{1}{3}B.h=\frac{1}{3}6a^2.4a=8a^3$."
        },
        {
            "question": "Trong không gian $Oxyz$, vecto nào dưới đây là một vecto chi phương của trục $Oy$?",
            "options": ["A. $\overrightarrow{j}=\left ( 0;1;0 \right )$", "B. $\overrightarrow{k}=\left ( 0;0;1 \right )$", "C. $\overrightarrow{u}=\left ( 1;0;1 \right )$", "D. $\overrightarrow{i}=\left ( 1;0;0 \right )$"],
            "answer": 0,
            "explanation": "Ta có một vecto chỉ phương của trục $Oy$ là $\overrightarrow{j}=\left ( 0;1;0 \right )$"
        },
        {
            "question": "Trong không gian $Oxyz$, cho mặt phẳng $ \left ( P \right ):2x-3y-2+\sqrt{2}=0$. Vecto nào dưới đây là một vecto pháp tuyến của $ \left ( P \right )$?",
            "options": ["A. $\overrightarrow{n_{2}}=\left ( 2;-3;-2 \right )$", "B. $\overrightarrow{n_{4}}=\left ( -2;3;-2 \right )$", "C. $\overrightarrow{n_{3}}=\left ( 2;3;-2 \right )$", "D. $\overrightarrow{n_{1}}=\left ( 2;-3;0 \right )$"],
            "answer": 3,
            "explanation": "Ta có một vecto pháp tuyến của $ \left ( P \right )$ là: $\overrightarrow{n}=\left ( 2;-3;0 \right )$."
        },
        {
            "question": "Trong không gian $Oxyz$, cho hai điểm $A\left ( 3;2;-4 \right )$ và $B\left ( 1;-4;5 \right )$. Tọa độ của vecto $\overrightarrow{AB}$ là",
            "options": ["A. $\left ( -2;-6;9 \right )$", "B. $\left ( 2;6;9 \right )$", "C. $\left ( -2;6;-9 \right )$", "D. $\left ( -2;6;-1 \right )$"],
            "answer": 0,
            "explanation": "Ta có $\overrightarrow{AB}=\left ( -2;-6;9 \right )$."
        },
        {
            "question": "Cho hàm số $f\left ( x \right )=\frac{1}{2x+1}$",
            "options": ["A. $\int f\left ( x \right )dx=ln\left|2x+1 \right|+C$", "B. $\int f\left ( x \right )dx=2ln\left|2x+1 \right|+C$", "C. $\int f\left ( x \right )dx=\frac{1}{2}ln\left|2x+1 \right|+C$", "D. $$"],
            "answer": 3,
            "explanation": "Ta có $\int f\left ( x \right )dx=\int \frac{1}{2x+1}dx=\frac{1}{2}ln\left|2x+1 \right|+C$"
        },
        {
            "question": "Tập nghiệm của bất phương trình $\left ( \frac{2}{3} \right )^{x}> \frac{9}{4}$ là",
            "options": ["A. $\left ( -\infty ;-2 \right )$", "B. $\left ( -\infty ;log_{2}3 \right )$", "C. $\left ( 2;+\infty  \right )$", "D. $\left ( -\infty ;-2 \right ]$"],
            "answer": 1,
            "explanation": "Ta có $\left ( \frac{2}{3} \right )^{x}> \frac{9}{4}$. Vậy tập nghiệm bất phương trình là $S=\left ( -\infty ;-2 \right )$."
        },
        {
            "question": "Cho khối lăng trụ có diện tích đáy bằng $12a^2$ và thể tích bằng $48a^3$. Chiều cao của khối lăng trụ đẫ cho bằng",
            "options": ["A. $4a^2$", "B. $4a$", "C. $12a$", "D. $6a$"],
            "answer": 1,
            "explanation": "Thể tích của lăng trụ đã cho là $V=B.h\Rightarrow h = \frac{V}{B}=\frac{48a^3}{12a^3}=4a$"
        },
        {
            "question": "Nếu $\int_{2}^{6}f(x)dx=10$ thì $\int_{1}^{3}f(2x)dx$ bằng",
            "options": ["A. $20$", "B. $30$", "C. $5$", "D. $15$"],
            "answer": 2,
            "explanation": "Đặt $t=2x\Rightarrow dt=2dx\Rightarrow dx=\frac{1}{2}dt$. \nĐổi cận: $x=1\Rightarrow t=2; x=3\Rightarrow t=6$. \nSuy ra $\int_{1}^{3}f(2x)dx=\frac{1}{2}\int_{2}^{6}f(t)dt=\frac{1}{2}\int_{2}^{6}f(x)dx=\frac{1}{2}.10=5$"
        },
        {
            "question": "Hàm số nào dưới đây đồng biến trên khoảng $\left ( 0;+\infty  \right )$?",
            "options": ["A. $y=log_{\frac{2}{3}}x$", "B. $y=log_{\frac{\sqrt{3}}{2}}x$", "C. $y=log_{\frac{\pi }{3}}x$", "D. $y=-log_{3}x$"],
            "answer": 2,
            "explanation": "Hàm số $y=log_{\frac{\pi }{3}}x$ có cơ số $\frac{\pi}{3}>1$ nên đồng biến trên khoảng $\left ( 0;+\infty  \right )$."
        },
        {
            "question": "Với $a$ là số thực dương tùy ý, $log_{\sqrt{3}}a^5$ bằng",
            "options": ["A. $\frac{5}{2}log_{3}a$", "B. $10log_{3}a$", "C. $5log_{3}a$", "D. $25log_{3}a$"],
            "answer": 1,
            "explanation": "Ta có $log_{\sqrt{3}}a^5=5log_{3^\frac{1}{2}}a=10log_{3}a$"
        },
        {
            "question": "Cho hàm số $y=x^3-3x^2-9x+2$. Hàm số đã cho nghịch biến trên khoảng nào sau đây?",
            "options": ["A. $\left ( -\infty ;1 \right )$", "B. $\left ( -1 ;3 \right )$", "C. $\left ( 3 ;+\infty \right )$", "D. $\left ( -2 ;3 \right )$"],
            "answer": 1,
            "explanation": "$y'=3x^2-6x-9$. \nGiải $y'< 0 \Leftrightarrow 3x^2-6c-9<0 \Leftrightarrow x\in \left ( -1 ;3 \right )$. \nVậy hàm số $y=x^3-3x^2-9x+2$ nghịch biến trên khoảng $\left ( -1 ;3 \right )$."
        },
        {
            "question": "Lớp 12A có 45 học sinh trong đó có 30 nam và 15 nữ. Có bao nhiêu cách chọn 3 bạn nam và 2 bạn nữ đại diện cho lớp đi nghe tư vấn tuyển sinh đại học?",
            "options": ["A. $4165$", "B. $425300$", "C. $426300$", "D. $5165$"],
            "answer": 2,
            "explanation": "Chọn 3 bạn nam từ 30 bạn nam có $C_{30}^{3}$ cách. \nChọn 2 bạn nam từ 15 bạn nam có $C_{15}^{2}$ cách. \n$\Rightarrow$ Số cách chọn 3 bạn nam và 2 bạn nữ đại diện cho lớp đi nghe tư vấn tuyển sinh đại học là: $C_{30}^{3}.C_{15}^{2}=426300$."
        },
        {
            "question": "Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật, $AB=2a, BC=4a, SA$ vuông góc với mặt phẳng đáy và $SA=2a$. Gọi M là trung điểm cạnh $SC$. Khoảng cách từ $M$ đến mặt phẳng $\left ( SBD \right )$ bằng.",
            "options": ["A. $\frac{2a}{3}$", "B. $3a$", "C. $\frac{3a}{2}$", "D. $\frac{4a}{3}$"],
            "answer": 0,
            "explanation": "Có $d\left ( M,\left ( SBD \right ) \right )=\frac{1}{2}d\left ( C,\left ( SBD \right ) \right )=\frac{1}{2}d\left ( A,\left ( SBD \right ) \right )$. \nKẻ $\left\{\begin{matrix}AI\perp BD\\AH\perp SI\end{matrix}\right.$ có $\left\{\begin{matrix}BD\perp AI\\BD\perp SA\end{matrix}\right. \Rightarrow BD\perp \left ( SAI \right )\Rightarrow BD\perp AH$. \n\left\{\begin{matrix}AH\perp BD\\AH\perp SI\end{matrix}\right.\Rightarrow AH\perp \left ( SBD \right )\Rightarrow d\left ( A,\left ( SBD \right ) \right )=AH$. \n$AI= \frac{AD.AB}{\sqrt{AD^2 + AB^2}}=\frac{2a.4a}{\sqrt{4a^2+16a^2}}=\frac{4a}{\sqrt{5}}$. \n$AI= \frac{SA.AI}{\sqrt{SA^2 + AI^2}}=\frac{2a.\frac{4a}{\sqrt{5}}}{\sqrt{4a^2+\frac{16}{5}a^2}}=\frac{4a}{\sqrt{3}}$. \n$\Rightarrow d\left ( M,\left ( SBD \right ) \right )=\frac{2a}{3}$."
        },
        {
            "question": "Cho số phức $z=6+2i$. Phần thực của số phức $\frac{\overline{z}}{1+i}$ bằng",
            "options": ["A. $2$", "B. $-4$", "C. $-2$", "D. $4$"],
            "answer": 0,
            "explanation": "$\frac{\overline{z}}{1+i}=\frac{6-2i}{1+i}=\frac{\left (6-2i \right ) \left (1-i \right )}{1-i^2}=\frac{4-8i}{2}=2-4i$. \n$\Rightarrow $Phần thực của số phức $\frac{\overline{z}}{1+i}$ bằng 2"
        },
        {
            "question": "Cho cấp số nhân $\left (u_{n} \right )$ với $u_{2}=3$ và $u_{5}=-192$. Công hội của cấp nhân đẫ cho bằng",
            "options": ["A. $4$", "B. $-4$", "C. $16$", "D. $-12$"],
            "answer": 1,
            "explanation": "Áp dụng công thức $u_{n}=u_{1}.q^{n-1}$ \nTa có $\left\{\begin{matrix}u_{2}=3\\u_{5}=-192\end{matrix}\right.\Leftrightarrow \left\{\begin{matrix}u_{1}.q=3\\q^{4}=-64\end{matrix}\right.\Leftrightarrow \left\{\begin{matrix}u_{1}=-\frac{3}{4}\\q=-4\end{matrix}\right.$. \nCông bội của cấp số nhân đã cho bằng -4."
        },
        {
            "question": "Đồ thị nào dưới đây có dạng như đường cong tronh hình vẽ bên?",
            "options": ["A. $y=-x^3-2x^2+1$", "B. $y=\frac{2x+1}{x+1}$", "C. $y=-x^4+2x^2-3$", "D. $y=x^3+3x+1$"],
            "answer": 3,
            "explanation": "Dễ thấy đồ thị trong hình là đồ thị của hàm số bậc 3 có 2 cực trị với hệ số a > 0. Do đó đồ thị hàm số cần tìm là: $y=x^3+3x+1$."
        },
        {
            "question": "Điểm M trong hình bên là điểm biểu diễn của số phức nào dưới đây?",
            "options": ["A. $2+3i$", "B. $-2-3i$", "C. $3-2i$", "D. $-2+3i$"],
            "answer": 3,
            "explanation": "Ta có điểm $M\left (-2;3 \right )$ là điểm biểu diễn của số phức $z=-2+3i$."
        },
        {
            "question": "Cho hàm số $y = f \left (x \right )$ có bảng biến thiên như hình vẽ. Giá trị cực đại của hàm số đã cho là:",
            "options": ["A. $2$", "B. $-2$", "C. $3$", "D. $-1$"],
            "answer": 2,
            "explanation": "Dựa vào bảng biến thiên ta thấy giá trị cực đại của hàm số đâ cho là 3."
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },
        {
            "question": "",
            "options": ["A. $$", "B. $$", "C. $$", "D. $$"],
            "answer": 1,
            "explanation": ""
        },

    ]
}

# Thêm câu hỏi vào MongoDB
collection.insert_one(questions_data)

