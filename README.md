# SyncAI 🎙️ → 📝

SyncAI is an intelligent speech-to-text transcription tool built on OpenAI's Whisper automatic speech recognition system. Featuring a user-friendly Streamlit interface, it provides accurate transcriptions with advanced features like pause detection and confidence scoring.

## ✨ Features

- **Modern Streamlit UI** - Clean, intuitive interface for batch audio file processing
- **Advanced Analysis**
  - Automatic pause detection
  - Word-level confidence scoring with color coding
  - Average confidence score calculation
- **Translation Support** - Direct translation to English
- **Privacy-First Design** 
  - Fully offline processing
  - No cloud uploads
  - Suitable for sensitive/clinical data

## 🖥️ Screenshots

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Start Screen</b></td>
      <td align="center"><b>Results View</b></td>
    </tr>
    <tr>
      <td><img src="https://raw.githubusercontent.com/whitedevil-glitch/syncai/main/imgs/start.png" alt="Start Screen"/></td>
      <td><img src="https://raw.githubusercontent.com/whitedevil-glitch/syncai/main/imgs/result.png" alt="Results Screen"/></td>
    </tr>
  </table>
</div>

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip
- Git
- PyTorch (`pip install torch torchvision torchaudio`)

### Installation

1. Clone the repository
```bash
git clone https://github.com/whitedevil-glitch/syncai
cd syncai
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Launch the application
```bash
streamlit run Transcribe.py
```

> 💡 **Tip**: Create a desktop shortcut for easy access by following [these instructions](https://discuss.streamlit.io/t/launching-streamlit-webapp-from-desktop-shortcut/26297)

## 📝 Usage Guide

1. Launch the application
2. Upload one or multiple audio files using the file picker
3. Select your preferred model:
   - Use "large" for highest accuracy
   - Use "small" or "medium" for faster processing
4. Configure additional parameters as needed
5. Process your files and download the transcripts
   - Transcripts are also automatically saved to the local `transcripts` folder

## ⚠️ Troubleshooting

| Error | Solution |
|-------|----------|
| Request failed with status code 403 | Run the app with the flag: `--server.enableWebsocketCompression=false` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Contact

For questions, feedback, or support:
- Email: saishankar2803@gmail.com
- GitHub Issues: [Create an issue](https://github.com/whitedevil-glitch/syncai/issues)

## 📚 Credits

SyncAI builds upon these excellent open-source projects:

- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition system
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio) - Audio analysis
- [Whisper UI](https://github.com/hayabhay/whisper-ui) - UI components
- [Whisper Streamlit](https://github.com/jojojaeger/whisper-streamlit) - Idea Inspiration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <i>Built with ❤️ as a college mini-project</i>
</div>
