import { Html, Head, Main, NextScript } from 'next/document'
import createEmotionServer from '@emotion/server/create-instance';
import theme from '@/utils/theme';

export default function Document() {
  return (
    <Html lang="ja">
      <Head>
        <meta name="theme-color" content={theme.palette.primary.main} />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
