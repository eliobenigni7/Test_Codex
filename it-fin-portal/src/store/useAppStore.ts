import { create } from 'zustand'

interface AppState {
  darkMode: boolean
  toggle: () => void
}

export const useAppStore = create<AppState>((set) => ({
  darkMode: false,
  toggle: () => set((s) => ({ darkMode: !s.darkMode })),
}))
