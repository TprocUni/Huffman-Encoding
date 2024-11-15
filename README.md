# Huffman-Encoding
This Python program implements **Huffman Encoding** for text compression and decompression. It supports reading sample text, calculating character frequencies, building Huffman trees, encoding/decoding files, and saving results. The program also includes the flexibility to use predefined encoding trees for different languages or create custom ones.


### Key Features

#### 1. Frequency Calculation
- **Function**: `calcFrequencies(sampleText)`
  - Counts the occurrences of each character in the input text.
  - Results are stored in a dictionary for further processing.

#### 2. Huffman Tree Construction
- **Function**: `transformToList(freqDict)`
  - Converts character frequencies into a heap-based structure using `heapq`.
  - Builds the Huffman tree by merging nodes and assigning binary codes to characters.
- **Function**: `transformToTree(huffmanList)`
  - Converts the Huffman list into a dictionary with characters mapped to binary codes.

#### 3. Encoding
- **Function**: `encodeFile(huffmanList)`
  - Encodes a string or text file using the selected Huffman tree.
  - Results are stored in a compressed binary format.

#### 4. Decoding
- **Function**: `decode(huffmanList)`
  - Decodes a binary file back into the original text using the corresponding Huffman tree.
  - Handles extra bits added due to byte alignment.

#### 5. Saving and Managing Encoding Trees
- **Function**: `selectEncodingTree(originalHuffmanList)`
  - Allows the user to switch between predefined trees (English, Finnish, French) or create a custom one.
- **Function**: `customEncoding()`
  - Generates a new Huffman tree from a string or `.txt` file.

#### 6. File Handling
- **Function**: `saveEncodedString(encodedString)`
  - Saves the encoded binary data to a file with a user-defined name or a default location.

#### 7. User Interaction
- A command-line interface (CLI) enables:
  - Encoding text or files.
  - Switching between encoding trees.
  - Decoding binary files back into text.

---

### Workflow Example

1. **Encoding a File**:
   - The user selects a file or inputs a string.
   - The program calculates character frequencies, builds a Huffman tree, and encodes the text.
   - Encoded binary data is saved to a file.

2. **Decoding a File**:
   - The user provides the binary file to decode.
   - Using the Huffman tree, the program reconstructs the original text.

3. **Switching Encoding Trees**:
   - The user selects a predefined tree (English, Finnish, or French) or creates a custom one from text or a file.

---

### Observations and Benefits

- **Compression Efficiency**:
  - Frequently occurring characters are assigned shorter binary codes, reducing storage requirements.
- **Flexibility**:
  - Supports multiple languages and custom trees for specific text datasets.
- **User-Friendly**:
  - CLI guides users through encoding, decoding, and managing trees with validation for inputs.

---

### Conclusion

This Huffman Encoding program provides a complete solution for text compression and decompression. Its modular design and extensible features make it suitable for educational purposes and practical applications in file size reduction.
