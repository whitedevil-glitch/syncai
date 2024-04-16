import streamlit as st
from transcriber import Transcription
import docx
from datetime import datetime
import pathlib
import io
import matplotlib.colors as mcolors

# app wide config
st.set_page_config(
    page_title="Whisper",
    layout="wide",
    page_icon="💬"
)

# load stylesheet
with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()),
                unsafe_allow_html=True)

# app sidebar for uplading audio files
with st.sidebar.form("input_form"):
    input_files = st.file_uploader(
        "Files", type=["mp4", "m4a", "mp3", "wav"], accept_multiple_files=True)

    whisper_model = st.selectbox("Whisper model", options=[
        "tiny", "base", "small", "medium", "large"], index=4)

    pauses = st.checkbox("Pause the transcriber", value=False)

    translation = st.checkbox("English translation", value=False)

    transcribe = st.form_submit_button(label="Start")

if transcribe:
    if input_files:
        st.session_state.transcription = Transcription(
            input_files)
        st.session_state.transcription.transcribe(
            whisper_model, translation
        )
    else:
        st.error("Please select a file")

# if there is a transcription, render it. If not, display instructions
if "transcription" in st.session_state:

    for i, output in enumerate(st.session_state.transcription.output):
        doc = docx.Document()
        avg_confidence_score = 0
        amount_words = 0
        save_dir = str(pathlib.Path(__file__).parent.absolute()
                       ) + "/transcripts/"
        st.markdown(
            f"#### Transcription from {output['name']}")
        for idx, segment in enumerate(output['segments']):
            for w in output['segments'][idx]['words']:
                amount_words += 1
                avg_confidence_score += w['probability']
        st.markdown(
            f"_(whisper model:_`{whisper_model}` -  _language:_ `{output['language']}` -  _⌀ confidence score:_ `{round(avg_confidence_score / amount_words,3)}`)")
        prev_word_end = -1
        text = ""
        html_text = ""
        # Define the color map
        colors = [(0.6, 0, 0), (1, 0.7, 0), (0, 0.7, 0)]
        cmap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

        with st.expander("Transcript"):
            color_coding = st.checkbox(
                "Color coding", value=False, key={i}, help="Color coding a word based on the probability that it was correctly recognized. The color scale ranges from green (high) to red (low).(More the green it is more confident the AI is!)")
            for idx, segment in enumerate(output['segments']):
                for w in output['segments'][idx]['words']:
                    # check for pauses in speech longer than 3s
                    if pauses and prev_word_end != -1 and w['start'] - prev_word_end >= 3:
                        pause = w['start'] - prev_word_end
                        pause_int = int(pause)
                        html_text += f'{"."*pause_int}{{{pause_int}sek}}'
                        text += f'{"."*pause_int}{{{pause_int}sek}}'
                    prev_word_end = w['end']
                    if (color_coding):
                        rgba_color = cmap(w['probability'])
                        rgb_color = tuple(round(x * 255)
                                          for x in rgba_color[:3])
                    else:
                        rgb_color = (0, 0, 0)
                    html_text += f"<span style='color:rgb{rgb_color}'>{w['word']}</span>"
                    text += w['word']
                    # insert line break if there is a punctuation mark
                    if any(c in w['word'] for c in "!?.") and not any(c.isdigit() for c in w['word']):
                        html_text += "<br><br>"
                        text += '\n\n'
            st.markdown(html_text, unsafe_allow_html=True)
            doc.add_paragraph(text)

        if (translation):
            with st.expander("English Trans-"):
                st.markdown(output["translation"], unsafe_allow_html=True)

        # save transcript as docx. in local folder
        file_name = output['name'] + "-" + whisper_model + \
            "-" + datetime.today().strftime('%d-%m-%y') + ".docx"
        doc.save(save_dir + file_name)

        bio = io.BytesIO()
        doc.save(bio)
        st.download_button(
            label="Download Transcript",
            data=bio.getvalue(),
            file_name=file_name,
            mime="docx"
        )

else:
    # show instruction page
    st.markdown("<h1>SyncAI: Your AI Subtitle Assistant </h1> <p>This project was created by <a href='mailto:saishankar2803@gmail.com'> Sai Shankar </a> " +
                "for college's mini-project </p><h2 class='highlight'>WHAT IS IT? </h2> <p>This project tool is based on the Whisper Automatic Speech Recogniton system (ARS) and is embedded into a Streamlit Web App.</p>""<h2 class='highlight'>Data Privacy: </h2> <ul><li>Whisper is used locally as well as offline (no internet connection needed)</li><li>Nothing is being uploaded to the cloud</li><li>Therefore safe clinical use</li></ul>"" <h2 class='highlight'>Features: </h2> <ul><li>Streamlit UI: The tool includes a user-friendly interface that allows you to upload multiple audio files and get a nicely formated transcript.</li><li>Streamlit UI: The tool includes a user-friendly interface that allows you to upload multiple audio files and get a nicely formated transcript.</li><li>Pause detection: The tool can detect pauses in the audio.</li><li>Confidence scores: The tool can color the words according to its probability and display the average score.</li><li>Translation to english</li><li>Speaker detection: not available</li></ul>" +
                "The transcripts are saved to a local directory on this PC.</p><h2 class='highlight'>USE: </h2> <ol><li> Select the files you would like to have transcribed (multiple files possible)</li>" +
                "<li>  Choose a model (<i>large</i> for the best result) and other parameters and click 'Start'</li> <li> View the resulting transcripts in <i>transcripts</i> folder of main directory</li><br>The Whisper architecture is a simple end-to-end approach, implemented as an encoder-decoder Transformer. Input audio is split into 30-second chunks, converted into a log-Mel spectrogram, and then passed into an encoder. A decoder is trained to predict the corresponding text caption, intermixed with special tokens that direct the single model to perform tasks such as language identification, phrase-level timestamps, multilingual speech transcription, and to-English speech translation.</ol>",
                unsafe_allow_html=True)
