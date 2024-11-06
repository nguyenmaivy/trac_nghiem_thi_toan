import streamlit as st
import random
import os
from pymongo import MongoClient

# Kết nối MongoDB Atlas
client = MongoClient('mongodb+srv://kvan185:123098mz@cluster0.ji7lv.mongodb.net/mydb?retryWrites=true&w=majority&appName=Cluster0')
db = client['math_quiz']
collection = db['quizzes']

# Hàm lấy các chủ đề từ MongoDB
def get_topics():
    return list(collection.find({}, {"topic": 1}))

# Hàm lấy câu hỏi theo chủ đề từ MongoDB
def get_questions(topic):
    return collection.find_one({"topic": topic})["questions"]

# Hàm kiểm tra và hiển thị ảnh
def display_image(image_filename):
    image_path = os.path.join('img', image_filename)
    if os.path.exists(image_path):  # Kiểm tra xem ảnh có tồn tại không
        st.image(image_path, caption="Ảnh câu hỏi", use_column_width=True)
    else:
        st.warning("Không tìm thấy ảnh cho câu hỏi.")

# Giao diện ứng dụng trắc nghiệm
st.title('Ứng dụng thi trắc nghiệm môn Toán')

# Kiểm tra nếu câu hỏi đã được lưu trong session_state
if 'selected_questions' not in st.session_state:
    # Lấy danh sách các chủ đề
    topics = get_topics()
    
    # Chọn chủ đề
    selected_topic = st.selectbox("Chọn chủ đề:", [topic['topic'] for topic in topics])
    
    # Lấy câu hỏi từ MongoDB cho chủ đề đã chọn
    questions = get_questions(selected_topic)
    
    # Lựa chọn ngẫu nhiên 40 câu hỏi (hoặc ít hơn nếu ít câu hỏi)
    num_questions = min(40, len(questions))
    selected_questions = random.sample(questions, num_questions)
    
    # Lưu câu hỏi đã chọn vào session_state
    st.session_state['selected_questions'] = selected_questions
    # Lưu đáp án của người dùng vào session_state
    st.session_state['user_answers'] = [None] * len(selected_questions)

# Lấy câu hỏi đã chọn từ session_state nếu có
selected_questions = st.session_state['selected_questions']
user_answers = st.session_state['user_answers']

# Hiển thị các câu hỏi
for i, question in enumerate(selected_questions):
    st.subheader(f"Câu {i+1}:")
    st.markdown(question['question']['ques'], unsafe_allow_html=True)  # Hiển thị câu hỏi dạng LaTeX

    # Nếu câu hỏi có ảnh, hiển thị ảnh
    if question['question']['image']:
        display_image(question['question']['image'])

    # Sử dụng session_state để lưu trạng thái của từng câu hỏi
    options = question['options']  # Giả định options là một danh sách
    if isinstance(options, dict):
        options = list(options.values())  # Chuyển đổi dict thành list nếu cần
    
    answer_index = options.index(user_answers[i]) if user_answers[i] is not None else None
    answer = st.radio(f"Chọn đáp án cho câu {i+1}",
                      options,
                      index=answer_index,
                      key=f"answer_{i}")

    # Lưu đáp án đã chọn vào session_state
    user_answers[i] = answer
    st.session_state['user_answers'] = user_answers

# Thêm nút để xóa cache
if st.button("Xóa cache"):
    st.cache_data.clear()
    st.success("Cache đã được xóa!")

# Nút để nộp bài
if st.button("Nộp bài"):
    correct_answers = 0
    
    # Kiểm tra đáp án
    for i, question in enumerate(selected_questions):
        if user_answers[i] == question['answer']['value']:  # Đảm bảo answer là số nguyên
            correct_answers += 1

    # Hiển thị kết quả
    st.write(f"Kết quả: {correct_answers}/{len(selected_questions)}")

    # Hiển thị giải thích cho từng câu hỏi
    for i, question in enumerate(selected_questions):
        st.write(f"Giải thích câu {i+1}:")
        st.markdown(question['answer']['explanation'], unsafe_allow_html=True)
