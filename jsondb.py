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
            "question": "Trong không gian $Oxyz$, cho mặt phẳng $$",
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

