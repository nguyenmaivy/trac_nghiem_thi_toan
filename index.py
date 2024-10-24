import streamlit as st
from pymongo import MongoClient

# Kết nối MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['math_quiz']
collection = db['quizzes']

# Hàm lấy các chủ đề từ MongoDB
def get_topics():
    return list(collection.find({}, {"topic": 1}))

# Hàm lấy câu hỏi theo chủ đề từ MongoDB
def get_questions(topic):
    return collection.find_one({"topic": topic})["questions"]

# Giao diện ứng dụng trắc nghiệm
st.title('Ứng dụng thi trắc nghiệm môn Toán')

# Lấy danh sách các chủ đề
topics = get_topics()

# Chọn chủ đề
selected_topic = st.selectbox("Chọn chủ đề:", [topic['topic'] for topic in topics])

# Lấy câu hỏi từ MongoDB cho chủ đề đã chọn
questions = get_questions(selected_topic)

# Biến lưu đáp án của học sinh trong session_state
if 'user_answers' not in st.session_state:
    st.session_state['user_answers'] = [None] * len(questions)  # None: chưa chọn đáp án nào

# Hiển thị các câu hỏi
for i, question in enumerate(questions):
    st.subheader(f"Câu {i+1}:")
    st.markdown(question['question'], unsafe_allow_html=True)  # Hiển thị câu hỏi dạng LaTeX
    
    # Sử dụng session_state để lưu trạng thái của từng câu hỏi
    options = question['options']  # Giả định options là một danh sách
    if isinstance(options, dict):
        options = list(options.values())  # Chuyển đổi dict thành list nếu cần
    
    answer_index = options.index(st.session_state['user_answers'][i]) if st.session_state['user_answers'][i] is not None else None
    answer = st.radio(f"Chọn đáp án cho câu {i+1}",
                      options,
                      index=answer_index,
                      key=f"answer_{i}")

    # Lưu đáp án đã chọn vào session_state
    st.session_state['user_answers'][i] = answer

# Thêm nút để xóa cache
if st.button("Xóa cache"):
    st.cache_data.clear()
    st.success("Cache đã được xóa!")

# Nút để nộp bài
if st.button("Nộp bài"):
    correct_answers = 0
    
    # Kiểm tra đáp án
    for i, question in enumerate(questions):
        if st.session_state['user_answers'][i] == question['options'][int(question['answer'])]:  # Đảm bảo answer là số nguyên
            correct_answers += 1

    # Hiển thị kết quả
    st.write(f"Kết quả: {correct_answers}/{len(questions)}")

    # Hiển thị giải thích cho từng câu hỏi
    for i, question in enumerate(questions):
        st.write(f"Giải thích câu {i+1}:")
        st.markdown(question['explanation'], unsafe_allow_html=True)
