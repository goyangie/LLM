import gradio as gr

def favorite_language(language):
    messages = {
        "허태웅 바보": "허태웅은 바보가 맞습니다! 바보라하면 빼 놓을 수 없는 인물입니다.",
        "허태웅 멍청이": "허태웅은 멍청이가 맞습니다! 멍청이중에서도 최고이지요. 전기 기능사 시험을 58.33점으로 떨어졌습니다!",
        "허태웅 똥개": "허태웅은 똥개가 맞습니다! 올바른 선택입니다.",
        "허태웅 쪼다": "허태웅은 쪼다가 맞습니다! 아주 탁월한 선택입니다."
    }
    return messages.get(language, '보기 중에서 선택하십시오.')

interface = gr.Interface(
    fn=favorite_language,
    inputs = gr.Radio(['허태웅 바보', '허태웅 멍청이', '허태웅 똥개', '허태웅 쪼다'], label='보기'),
    outputs = 'text',
    title='보기',
    description='라디오 버튼에서 동의하는 것을 체크하시오.'
)

interface.launch()