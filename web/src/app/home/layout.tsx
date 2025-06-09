'use client';

import styles from './layout.module.css';
import HomeSidebar from '@/app/home/components/home-sidebar/HomeSidebar';
import HomeTitleBar from '@/app/home/components/home-titlebar/HomeTitleBar';
import React, { useState } from 'react';
import { SidebarChildVO } from '@/app/home/components/home-sidebar/HomeSidebarChild';
import { I18nLabel } from '@/app/infra/entities/common';
import { SidebarProvider, SidebarInset } from '@/components/ui/sidebar';
import { AppSidebar } from '@/app/home/components/app-sidebar/app-sidebar';

export default function HomeLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [title, setTitle] = useState<string>('');
  const [subtitle, setSubtitle] = useState<string>('');
  const [helpLink, setHelpLink] = useState<I18nLabel>({
    en_US: '',
    zh_Hans: '',
  });
  const onSelectedChangeAction = (child: SidebarChildVO) => {
    setTitle(child.name);
    setSubtitle(child.description);
    setHelpLink(child.helpLink);
  };

  return (
    <SidebarProvider className={styles.homeLayoutContainer}>
      <AppSidebar />
      <SidebarInset>
        <HomeTitleBar title={title} subtitle={subtitle} helpLink={helpLink} />
        <main className={styles.mainContent}>{children}</main>
      </SidebarInset>
    </SidebarProvider>
  );
}
