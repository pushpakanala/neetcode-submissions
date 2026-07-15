class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for sentence in strs:
            if sentence == "":
                encoded.append("<EMPTY>")
            else:
                encoded.append(sentence)

            encoded.append("<EOS>")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        for sentence in s.split("<EOS>"):
            if sentence == "<EMPTY>":
                decoded.append("")
            elif sentence != "":
                decoded.append(sentence)

        return decoded

