import webview
import os
from datetime import datetime

class Api:
    def save_answers(self, answer_text):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_text = f"\n\n[JAWABAN BARU - {timestamp}]\n{answer_text}\n{'='*50}"
            with open('questions_data.txt', 'a', encoding='utf-8') as file:
                file.write(formatted_text)            
            return {'success': True, 'message': 'Jawaban berhasil disimpan!'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def check_file_exists(self):
        return os.path.exists('questions_data.txt')
    
    def create_file_if_not_exists(self):
        try:
            if not self.check_file_exists():
                with open('questions_data.txt', 'w', encoding='utf-8') as file:
                    file.write("DATA JAWABAN KUIS PSIKOLOGI DAN FILOSOFI\n")
                    file.write("=" * 50 + "\n")
                return {'success': True, 'message': 'File berhasil dibuat!'}
            else:
                return {'success': True, 'message': 'File sudah ada!'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

def main():
    html_file = 'questions.html'
    api = Api()
    api.create_file_if_not_exists()
    webview.create_window(
        title='Kuis Psikologi dan Filosofi',
        url=html_file,
        js_api=api,
        width=1840,
        height=920,
        min_size=(600, 600),
        resizable=True,
        shadow=True,
    )
    webview.start(debug=True)

if __name__ == '__main__':
    main()