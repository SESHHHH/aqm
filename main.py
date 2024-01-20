from semetrics import composite

clean_audio = input('clean: ')
enhanced_audio = input('enhanced: ')

[pesq_score, csig, cbak, covl, ssnr] = composite(clean_audio, enhanced_audio)

print(f'PESQ: {pesq_score}',
      f'CSIG: {csig}',
      f'CBAK: {cbak}',
      f'COVL: {covl}',
      f'SSNR: {ssnr}', sep='\n')
