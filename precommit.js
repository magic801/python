function verify(raw, sourceFile) {
    console.log(raw)
    console.log(sourceFile)
    throw new Error('test.')
}

module.exports = verify